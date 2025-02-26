from Transactions.package.Errors import ProcessAborted
from Transactions.package import Config
import os
import stat
import shutil

permissionHistory = dict()

def modifyPermissions(permissions, *paths):
    if not Config.FORCE_PERMISSIONS:
        return
    
    global permissionHistory

    for path in paths:
        if path == None:
            continue
        
        if not os.path.exists(path):
            continue
        
        permissionHistory[path] = os.stat(path).st_mode
        
        os.chmod(path, permissions)

def restorePermissions():
    global permissionHistory

    for path, permission in permissionHistory.items():
        if not os.path.exists(path):
            continue
        
        try:
            os.chmod(path, permission)
        except:
            # If an exception occurs here, that means that another
            # exception has already occurred in try_catch_wrapper
            # and error log kept. Just pass...
            pass

def try_catch_wrapper(addr1:str, func, addr2:str = None) -> None:
    global permissionHistory

    try:
        modifyPermissions(stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO,
                          addr1, addr2)
        
        if Config.MAX_OPERATION_LIMIT == 0:
            raise ProcessAborted("Max operation limit exceeded!")
        
        elif addr2 == None: func(addr1); addr2 = ""

        else: func(addr1, addr2)

    except OSError as e:
        if e.winerror != None:
            Config.addError(e.args, addr1, addr2)
        else:
            Config.addError(str(e))
    
    except (shutil.Error, PermissionError) as e:
        Config.addError(str(e), addr1, addr2)
    
    finally:
        Config.MAX_OPERATION_LIMIT -= 1

        restorePermissions()

        permissionHistory.clear()


# END