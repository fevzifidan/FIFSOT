from Transactions.package.Errors import CompletedProcessWithMissingItems, ERRCODE
from Transactions.package import Wrapper, Controller, Symlink, Config
from Transactions.package.ConditionControl import condition_control
import os

def remove_empty_directories(obj_addr:str, in_symlink_ok:bool=False, recursive:bool=True) -> None:
    
    with os.scandir(obj_addr) as directory:
        for item in directory:
            if Controller.is_special_file(item.path):
                Config.addError(ERRCODE["SpecialFile"], item.path)
                continue
            elif os.path.isdir(item.path):
                if not any(os.scandir(item.path)):
                    Wrapper.try_catch_wrapper(item.path, os.rmdir)
                elif recursive:
                    remove_empty_directories(item.path, in_symlink_ok, recursive)
                    if not any(os.scandir(item.path)):
                        Wrapper.try_catch_wrapper(item.path, os.rmdir)
    
    if len(Config.ERRORS) != 0:
        raise CompletedProcessWithMissingItems(Config.ERRORS)


def deleter(obj_addr:str, params:dict, only_content:bool, recursive:bool) -> None:

    if Controller.is_special_file(obj_addr) == True:
        Config.addError(ERRCODE["SpecialFile"], obj_addr)
        return

    elif os.path.islink(obj_addr) and condition_control(obj_addr, params):
        target = Symlink.delete_symlink(obj_addr, follow_symlinks=params["follow_symlinks"])
        if target != None:
            deleter(target, params, only_content=False, recursive=recursive)
        return

    elif os.path.isdir(obj_addr):
        if recursive == False and obj_addr != Config.DIRECTORY_TO_LEAVE_ADDRESS:
            return
        
        if any(os.scandir(obj_addr)):
            with os.scandir(obj_addr) as directory:
                for item in directory:
                    deleter(item.path, params, only_content = False, recursive=recursive)
        
        # If the content is completely deleted, consider whether the directory itself should be deleted as well.
        if not any(os.scandir(obj_addr)) and params["only_files"] == False:
            if Config.DIRECTORY_TO_LEAVE_ADDRESS == obj_addr and only_content == False:
                Wrapper.try_catch_wrapper(obj_addr, os.rmdir)
            elif Config.DIRECTORY_TO_LEAVE_ADDRESS != obj_addr and condition_control(obj_addr, params):
                Wrapper.try_catch_wrapper(obj_addr, os.rmdir)

    else:
        # If it is a file
        if condition_control(obj_addr, params):
            Wrapper.try_catch_wrapper(obj_addr, os.remove)


def delete(obj_addr:str, only_files:bool = False, in_symlink_ok:bool = False,
           follow_symlinks:bool = False, only_content:bool = True, recursive:bool = False,
           cond:dict = None) -> None:

    Config.ERRORS.clear()

    params = dict()
    params.update(locals().copy())
    params.update(cond.copy())

    Config.DIRECTORY_TO_LEAVE_ADDRESS = obj_addr

    Config.setMaxOperationLimit(obj_addr)
    
    deleter(obj_addr, params, only_content, recursive)

    if len(Config.ERRORS) != 0:
        raise CompletedProcessWithMissingItems(f"{Config.ERRORS}")


# END