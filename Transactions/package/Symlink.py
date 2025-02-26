from Transactions.package.Errors import *
from Transactions.package import Controller, Wrapper, Config
import subprocess
from os import path, symlink, readlink
from os.path import commonpath, abspath

def delete_symlink(obj_addr:str, recurse:bool=True, include:str=None,
                   exclude:str=None, force:bool=False, in_symlink_ok:bool = False,
                   follow_symlinks:bool = False) -> str|None:
    
    if not path.exists(obj_addr):
        raise SourceNotFoundError(obj_addr)
    
    if not path.islink(obj_addr):
        raise NotASymlinkError(obj_addr)
    
    if Controller.in_symlink(obj_addr) and in_symlink_ok == False:
        raise InSymlinkError(obj_addr, "delete_symlink")
    
    symlink_target = None

    if follow_symlinks == True:
        symlink_target = readlink(obj_addr)
    
    try:
        command = fr'Remove-Item "{obj_addr}"'

        if recurse:
            command += fr' -Recurse'
        if include:
            command += fr' -Include "{include}"'
        if exclude:
            command += fr' -Exclude "{exclude}"'
        if force:
            command += fr' -Force'

        subprocess.run(['powershell', '-Command', command], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
    except Exception as e:
        raise ProcessAborted(e.args)
    
    return symlink_target

def create_symlink(src:str, dest:str) -> None:

    if Controller.isAdmin() == False: raise NotAnAdminError("create_symlink")

    if not path.exists(src): raise SourceNotFoundError(src)

    if path.exists(dest): raise Exception("The destination should not exist!")

    if Controller.samefile(src, dest): raise SameFileError(src, dest)

    if Controller.is_special_file(src): raise SpecialFileError(address=src)

    if path.isdir(src) and path.splitext(dest)[1] != "":
        raise NotADirectoryError("The destination cannot be a file when the source is a directory!")
    
    if commonpath([abspath(src)]) == commonpath([abspath(src), abspath(dest)]):
        raise LoopError(addt_info=f"src -> {src} -- dest -> {dest}")

    if Controller.in_symlink(dest):
        raise NestedSymlinkError(dest)
    
    else:
        Wrapper.try_catch_wrapper(src, symlink, dest)
    
    if len(Config.ERRORS) != 0:
        raise CompletedProcessWithMissingItems(Config.ERRORS)


# END