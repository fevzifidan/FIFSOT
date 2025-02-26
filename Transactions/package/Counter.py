from Transactions.package.Errors import SourceNotFoundError
from Transactions.package.ConditionControl import condition_control
from Transactions.package.Controller import is_special_file
from Transactions.package import Config
from os import path, scandir, readlink

def count(addr:str, only_files:bool = False, recursive:bool = False,
          follow_symlinks:bool = False, cond:dict = None) -> int:
    
    cond = Config.COND if cond == None else cond
    
    if not path.exists(addr):
        raise SourceNotFoundError(addr)
    if is_special_file(addr):
        return 0
    if not path.isdir(addr):
        if path.isfile(addr):
            return 1
        else:
            return 0
    
    params = dict()
    params.update(locals().copy())
    params.update(cond.copy())
    counter = 0
    
    with scandir(addr) as directory:
        for item in directory:
            address = item.path
            if is_special_file(address):
                continue
            elif condition_control(address, params) == False:
                continue
            elif path.isfile(address):
                counter += 1
            elif path.isdir(address):
                if only_files == False:
                    counter += 1
                if recursive == True:
                    if path.islink(address) and follow_symlinks == True:
                        counter += count(readlink(address), only_files, recursive, follow_symlinks, cond)
                    elif path.islink(address) and follow_symlinks == False:
                        continue
                    else:
                        counter += count(address, only_files, recursive, follow_symlinks, cond)

    return counter


# END