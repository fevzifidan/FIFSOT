from Transactions.package.Errors import CompletedProcessWithMissingItems, ERRCODE, InSymlinkError
from Transactions.package import Wrapper, Controller, Symlink, Config
from Transactions.package.ConditionControl import condition_control
import os

def remove_empty_directories(obj_addr:str, in_symlink_ok:bool=False, recursive:bool=True) -> None:
    
    with os.scandir(obj_addr) as directory:
        for item in directory:
            if os.path.isdir(item.path):
                if not any(os.scandir(item.path)):
                    Wrapper.try_catch_wrapper(item.path, os.rmdir)
                elif recursive:
                    remove_empty_directories(item.path, in_symlink_ok, recursive)
                    if not any(os.scandir(item.path)):
                        Wrapper.try_catch_wrapper(item.path, os.rmdir)
    
    if len(Config.ERRORS) != 0:
        raise CompletedProcessWithMissingItems(Config.ERRORS)


def deleter(obj_addr:str, params:dict, only_content:bool, recursive:bool) -> None:

    if Controller.is_special_file(obj_addr):
        Config.addError(ERRCODE["SpecialFile"], obj_addr)
        return
    
    elif os.path.isdir(obj_addr):
        if obj_addr != Config.DIRECTORY_TO_LEAVE_ADDRESS:
            if not recursive:
                return
            
            elif not params["filterOnlyForFiles"] and not condition_control(obj_addr, params):
                return
        
        if os.path.islink(obj_addr):
            Config.addError(ERRCODE["Cannot call delete on a symlink directory!"], obj_addr)
        
        else:
            with os.scandir(obj_addr) as directory:
                for item in directory:
                    deleter(item.path, params, only_content = False, recursive=recursive)
            
            # If the content is completely deleted, consider whether the directory itself should be deleted as well.
            if not any(os.scandir(obj_addr)):
                if Config.DIRECTORY_TO_LEAVE_ADDRESS != obj_addr or not only_content:
                    Wrapper.try_catch_wrapper(obj_addr, os.rmdir)
        
    else:
        if not condition_control(obj_addr, params):
            return
        
        elif os.path.islink(obj_addr):
            target = Symlink.delete_symlink(obj_addr, follow_symlinks=params["follow_symlinks"])
        
            if target != None:
                # Whether target is None or not depends on follow_symlinks parameter.
                # If not None, delete the source of the link as well.
                deleter(target, params, only_content=False, recursive=recursive)
            
            return
        
        else:
            Wrapper.try_catch_wrapper(obj_addr, os.remove)


def delete(obj_addr:str, in_symlink_ok:bool = False, follow_symlinks:bool = False,
           only_content:bool = True, recursive:bool = False, cond:dict = Config.COND) -> None:

    Config.ERRORS.clear()

    params = dict()
    params.update(locals().copy())
    params.update(cond.copy())

    if not in_symlink_ok and Controller.in_symlink(obj_addr):
        raise InSymlinkError(obj_addr, "delete")
    
    elif os.path.islink(obj_addr):
        raise Exception("Cannot call delete operation on a symlink directory itself!")

    Config.DIRECTORY_TO_LEAVE_ADDRESS = obj_addr

    Config.setMaxOperationLimit(obj_addr)
    
    deleter(obj_addr, params, only_content, recursive)

    if len(Config.ERRORS) != 0:
        raise CompletedProcessWithMissingItems(f"{Config.ERRORS}")


# END