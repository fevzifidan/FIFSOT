"""
-> Developed by Fevzi FIDAN <-

This module has been programmed to run only on 'Windows' operating system and tested only on 'Windows 10'.

It provides some functions which have high-level and wide-ranging control parameters that allow you to perform operations on files and directories.

Some functions and features may require admin privileges.

This module is still under development. It may act inconsistent, make mistakes, and act unexpectedly.
It is strongly recommended you to make sure before performing irreversible transactions on important files and directories.
"""

__all__ = ["copy", "delete", "count", "rename" ,"create_symlink",
           "delete_symlink", "in_symlink", "remove_empty_directories"]

try:
    import os
    from os import path
    from Transactions.package.Errors import *
    from Transactions.package import *
except ImportError:
    raise Exception("One or more crucial modules for 'Directory_Transactions' to work could not be imported!")

if os.name != "nt":
    raise OSError("This module has been programmed to run only on the 'Windows' operating system!")

class Transaction:

    def __init__(self):
        # Temp gives the path corresponding to temp id
        # Temp id is uniquely created during runtime
        # by relevant functions
        self.temp = dict()

    def detectFileHolder(self, file_path:str|list) -> dict[str,tuple[str,int]]|None:
        if not isinstance(file_path, (str, list)):
            raise WrongParameterError(f"detectFileHolder got an invalid file_path param!")
        
        elif isinstance(file_path, list):
            Controller.validateParam(file_path, (str, ...))

            for index in range(len(file_path)):
                file_path[index] = Controller.getNormalizedPath(file_path[index])
        
        else:
            file_path = Controller.getNormalizedPath(file_path)

        return Detect.detectFileHolder(file_path)
    
    def terminateProcess(self, pid:int, file:str) -> bool:
        Controller.validateParam((pid, file), (int, str))

        file = Controller.getNormalizedPath(file)

        if not Detect.checkFilePIDMatch(pid, file):
            return False
        
        return Detect.terminateProcess(pid)

    def setCond(self, extension:None|str = None, name_startswith:None|str = None, contains:None|str = None,
            excl_startswith:None|str = None, excl_contains:None|str = None, case_insensitive:bool = False) -> None:
    
        Config.COND = {"extension":extension, "name_startswith":name_startswith, "contains":contains,
                       "excl_startswith":excl_startswith, "excl_contains":excl_contains, "case_insensitive":case_insensitive}

    def copy(self, src:str, dest:str, only_files:bool = False, merge_content_only:bool = False,
             skip_existing_ones:bool = False, symlinks:bool = False, cond:dict = None,
             copyMetaData:bool = True, recursive:bool = True) -> None:
        
        Controller.validateParam((src, dest, only_files, merge_content_only, skip_existing_ones, symlinks, copyMetaData),
                                 (str, str, bool, bool, bool, bool, bool))
        
        src = Controller.getNormalizedPath(src)
        dest = Controller.getNormalizedPath(dest)
        
        Copy.copy(src, dest, only_files, merge_content_only, skip_existing_ones,
                  symlinks, cond, copyMetaData, recursive)
    
    def delete(self, obj_addr:str, only_files:bool = False, in_symlink_ok:bool = False,
               follow_symlinks:bool = False, only_content:bool = True, recursive:bool = False,
               cond:dict = None, forcePermissions:bool = True) -> None:
        
        """
        If the "only_files" parameter is set to True, the directories themselves will not be deleted,
        even if all their contents are emptied.

        The "recursive" parameter determines whether to search subdirectories for objects to be deleted.
        When given False, subdirectories are not deleted.
        """

        obj_addr = Controller.getNormalizedPath(obj_addr)
    
        if not os.path.exists(obj_addr):
            raise SourceNotFoundError(obj_addr)
        
        if Controller.in_symlink(obj_addr) and in_symlink_ok == False:
            raise InSymlinkError(obj_addr, "delete")
        
        if not isinstance(cond, dict) and not cond == None:
            raise Exception(f"The parameter 'cond' must be a dict or None to use defaults!")
        
        if cond == None: cond = Config.COND

        Config.FORCE_PERMISSIONS = forcePermissions

        Delete.delete(obj_addr, only_files, in_symlink_ok, follow_symlinks, only_content, recursive, cond)
    
    def delete_symlink(self, obj_addr:str, recurse:bool=True, include:str=None,
                       exclude:str=None, force:bool=False, in_symlink_ok:bool = False,
                       follow_symlinks:bool = False) -> str|None:
        
        obj_addr = Controller.getNormalizedPath(obj_addr)
        
        Symlink.delete_symlink(obj_addr, recurse, include, exclude, force, in_symlink_ok, follow_symlinks)
    
    def remove_empty_directories(self, obj_addr:str, in_symlink_ok:bool=False, recursive:bool=True) -> None:

        Controller.validateParam((obj_addr, in_symlink_ok, recursive), (str, bool, bool))

        obj_addr = Controller.getNormalizedPath(obj_addr)
        
        if not os.path.exists(obj_addr):
            raise SourceNotFoundError(obj_addr)
        
        if Controller.is_special_file(obj_addr): raise SpecialFileError()

        if not os.path.isdir(obj_addr):
            raise NotADirectoryError("The obj_addr must be a directory!")
        
        if Controller.in_symlink(obj_addr) and in_symlink_ok == False:
            raise InSymlinkError(obj_addr, "remove_empty_directories")
        
        Config.setMaxOperationLimit(obj_addr)

        Delete.remove_empty_directories(obj_addr, in_symlink_ok, recursive)

    def create_symlink(self, src:str, dest:str):
        Controller.validateParam((src, dest), (str, str))

        src = Controller.getNormalizedPath(src)
        dest = Controller.getNormalizedPath(dest)

        Config.MAX_OPERATION_LIMIT = 1 # 1 operation is enough to create a symlink

        Symlink.create_symlink(src, dest)

    def count(self, addr:str, only_files:bool = False, recursive:bool = False,
                follow_symlinks:bool = False, cond:dict = None) -> int:
        
        if not isinstance(cond, dict) and not cond == None:
            raise Exception(f"The parameter 'cond' must be a dict or None to use defaults!")
        
        Controller.validateParam((addr, only_files, recursive, follow_symlinks),
                                 (str, bool, bool, bool))
        
        addr = Controller.getNormalizedPath(addr)
        
        counter = Counter.count(addr, only_files, recursive, follow_symlinks, cond)

        return counter

    def rename(self, address:str, prefix:str = "", suffix:str = "", only_files:bool = True,
                case:Rename.SortType = "Alphabetical", rev:bool = False, start:int = 0, zfill:int = 1) -> None:

        Controller.validateParam((address, prefix, suffix, case, start, zfill, only_files, rev),
                                 (str, str, str, str, int, int, bool, bool))
        
        address = Controller.getNormalizedPath(address)

        if not path.isdir(address):
            raise NotADirectoryError(f"The address must point to a directory! >> {address}")

        if zfill < 1:
            raise WrongParameterError(msg = f"'zfill' must be greater than or equal to 1! >> {zfill})")
        
        Config.setMaxOperationLimit(address)
        
        Rename.rename(address, prefix, suffix, only_files, case, rev, start, zfill)
    
    def create_archive(self, base_name:str, format:Archive.formats, root_dir:str, base_dir:str|None = None) -> str:
        Controller.validateParam(param = (base_name, root_dir), paramType = (str, str))

        base_name = Controller.getNormalizedPath(base_name)
        root_dir = Controller.getNormalizedPath(root_dir)
        base_dir = Controller.getNormalizedPath(base_dir)


        if not os.path.splitext(base_name)[1] == "":
            msg = "base_name should equal to the desired address, containing zip name without extension."
            raise WrongParameterError(msg = msg)
        
        base_dir_type = type(base_dir)
    
        if base_dir is not None and base_dir_type != str:
            raise WrongParameterError(msg = f"base_dir can be an str or None! -> type: {type(base_dir)}")
        
        # format will be controlled in create_archive in Archive module.
        
        return Archive.create_archive(base_name = base_name, format = format,
                                      root_dir = root_dir, base_dir = base_dir)


if __name__ == "__main__":
    pass


# END