from Transactions.package.Errors import *
from Transactions.package import Controller, Config, Wrapper, Delete, Symlink
from Transactions.package.ConditionControl import condition_control
from os import path, mkdir, makedirs, readlink, symlink, scandir
from os.path import commonpath, abspath
import shutil
import filecmp


def copier(src:str, dest:str) -> None:
    Wrapper.try_catch_wrapper(src, Config.COPY_FUNCTION, dest)

    if filecmp.cmp(src, dest, shallow=False) == False:
        status = "deleted"
        try:
            Delete.delete(dest)
        except Exception as e:
            status = "could not be deleted"
            pass

        Config.addError(f"A file was copied inconsistently! Copied faulty file {status}!")


def walker(src:str, dest:str, params:dict, recursive:bool) -> None:
    if Controller.is_special_file(src, dest):
        Config.addError(ERRCODE["SpecialFile"])
        return
    
    destination_exists = path.exists(dest)

    srcName = path.split(src)[1]
    destName = path.split(dest)[1]

    if path.islink(src):
        linkto = readlink(src)

        if path.isfile(src):
            if not destination_exists:
                if params["symlinks"]:
                    Wrapper.try_catch_wrapper(linkto, symlink, dest)
                else:
                    copier(linkto, dest)
            
            elif path.isdir(dest):
                walker(src, path.join(dest, srcName), params, recursive)
            
            elif params["skip_existing_ones"]:
                return
            
            else:
                if not params["symlinks"]:
                    copier(linkto, dest)
                
                else:
                    if (path.islink(dest) and readlink(dest) == linkto) or dest == linkto:
                        Config.addError(ERRCODE["SymLinkCycle"])
                    
                    else:
                        Delete.delete(dest, in_symlink_ok=True)
                        Wrapper.try_catch_wrapper(linkto, symlink, dest)

        else:
            if not params["symlinks"]:
                if not recursive:
                    return
                elif not path.exists(dest):
                    Wrapper.try_catch_wrapper(dest, makedirs)
                    walker(linkto, dest, params, recursive)
                else:
                    walker(src, dest, params, recursive)
            else:
                if not destination_exists:
                    Wrapper.try_catch_wrapper(linkto, symlink, dest)
                
                elif params["skip_existing_ones"]:
                    return
                
                elif path.islink(dest):
                    if readlink(dest) == linkto or dest == linkto:
                        Config.addError(ERRCODE["SymLinkCycle"])
                    
                    else:
                        Symlink.delete_symlink(dest)
                        Wrapper.try_catch_wrapper(linkto, symlink, dest)
                
                else:
                    Delete.delete(dest)
                    Wrapper.try_catch_wrapper(linkto, symlink, dest)


    elif path.isfile(src):
        if not condition_control(src, params): return

        elif not path.exists(dest):
            copier(src, dest)

        elif path.isdir(dest):
            copier(src, path.join(dest, srcName))

        elif params["skip_existing_ones"] == False:
            copier(src, dest)
        
        else: return

    else:
        with scandir(src) as directory:
            for item in directory:
                src_address = item.path
                dst_address = path.join(dest, item.name)

                if Controller.is_special_file(src_address) or not condition_control(src_address, params):
                    continue

                if path.isdir(src_address):
                    if not recursive: continue

                    elif params["only_files"]: continue

                    elif not path.exists(dst_address):
                        if not path.islink(src_address) or not params["symlinks"]:
                            Wrapper.try_catch_wrapper(dst_address, mkdir)
                        
                        elif path.islink(src_address) and params["symlinks"]:
                            dst_address = dest
                    
                    else:
                        pass

                walker(src_address, dst_address, params, recursive)


def copy(src:str, dest:str, only_files:bool = False, merge_content_only:bool = False,
         skip_existing_ones:bool = False, symlinks:bool = False, cond:dict = None,
         copyMetaData:bool = True, recursive:bool = True) -> None:
    
    if symlinks and not Controller.isAdmin(): raise NotAnAdminError("copy_symlink")

    if not isinstance(cond, dict) and cond != None:
        raise Exception(f"The parameter 'cond' must be a dict or None to use defaults!")
    
    cond = Config.COND if cond == None else cond
    
    Config.ERRORS.clear()

    if not path.exists(src): raise SourceNotFoundError(src)
    if Controller.samefile(src, dest): raise SameFileError(src, dest)
    if path.split(src)[0] == dest: raise SelfOverWrittenError()

    # If source and/or destination is a kind of special file, throws SpecialFileError
    if Controller.is_special_file(src, dest): raise SpecialFileError()

    if path.isdir(src) and path.splitext(dest)[1] != "":
        raise NotADirectoryError("The destination cannot be a file when the source is a directory!")
    
    if commonpath([abspath(src)]) == commonpath([abspath(src), abspath(dest)]):
        raise LoopError(addt_info=f"src -> {src} -- dest -> {dest}")
    
    if path.islink(src):
        linkto = readlink(src)
        if (path.exists(dest) and path.islink(dest) and readlink(dest) == linkto) or dest == linkto:
            raise Exception("A symlink cannot be copied over another symlink with the same source link or over its source!")
    
    if not copyMetaData: Config.COPY_FUNCTION = shutil.copy

    Config.setMaxOperationLimit(src)

    params = dict()
    params.update(locals().copy())
    params.update(cond.copy())

    if not path.exists(dest):
        if path.splitext(dest)[1] == "":
            makedirs(dest)
        elif not path.exists(path.split(dest)[0]):
            makedirs(path.split(dest)[0])

    if path.isdir(dest) and merge_content_only == False:
        if not path.islink(src) or symlinks == False:
            if path.isdir(src):
                dest = path.join(dest, path.split(src)[1])
                if not path.exists(dest): mkdir(dest)
    
    walker(src, dest, params, recursive)

    if len(Config.ERRORS) != 0:
        raise CompletedProcessWithMissingItems(Config.ERRORS)


# END