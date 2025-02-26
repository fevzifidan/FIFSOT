import os
from os.path import normcase, abspath
import stat
from pathlib import Path
from Transactions.package.Errors import WrongParameterError, UnsuitablePathError
from Transactions.package import Controller
from ctypes import windll

def is_special_file(*args) -> bool:
    for item in args:
        try:
            st = os.stat(item)
            mode = st.st_mode
        except OSError:
            # File most likely does not exist
            pass
        else:
            # Checks for other special files
            if stat.S_ISFIFO(mode): # FIFO (named pipe)
                return True
            elif stat.S_ISCHR(mode): # character special device file
                return True
            elif stat.S_ISBLK(mode): # block special device file
                return True
            elif stat.S_ISSOCK(mode): # a socket
                return True
    return False


def isRootedPath(*paths):
    status = True
    for path in paths:
        p = Path(path)
        if p.drive == "":
            status = False
    
    return status


def getNormalizedPath(path):
    if path is None: return path
    
    if os.path.islink(path):
        p = Path(path).absolute()
    
    else:
        p = Path(path).resolve()

    if not isRootedPath(path):
        raise UnsuitablePathError(f"Original path -> {path} -- Normalization -> {str(p)}")
    
    return str(p)


def samefile(src:str, dest:str) -> bool:
    return (normcase(abspath(src)) == normcase(abspath(dest)))


def in_symlink(obj_addr:str) -> bool:
    """
    If the file or directory whose address is given is actually inside a directory which
    is a symlink, it returns True. Otherwise, returns False. This control mechanism prevents
    files and directories, which are under a symlink, from uncontrollably handling from its
    source and all the locations which are linked to the same source.
    """
    Controller.validateParam(obj_addr, str)
    obj_addr = getNormalizedPath(obj_addr)

    divided_address = obj_addr.split(os.sep)
    united_address = divided_address[0]

    if united_address.endswith(':'): united_address += os.sep
    index = 1
    control = False

    while index < len(divided_address) - 1:
        united_address = os.path.join(united_address, divided_address[index])
        if os.path.islink(united_address):
            control = True
            break
        index += 1

    return control


def validateParam(param, paramType):
    if isinstance(param, (tuple, list)) and isinstance(paramType, (tuple, list)):
        if isinstance(paramType[1], type(Ellipsis)):
            for parameter in param:
                if not isinstance(parameter, paramType[0]):
                    raise WrongParameterError(f"Wrong '{parameter}' given! Must be {paramType[0]}!")
        
        else:
            for parameter, parameterType in zip(param, paramType):
                if not isinstance(parameter, parameterType):
                    raise WrongParameterError(f"Wrong '{parameter}' given! Must be {parameterType}!")

    elif not isinstance(param, paramType):
        raise WrongParameterError(f"Wrong '{param}' given! Must be {paramType}!")


def isAdmin() -> bool:
    return windll.shell32.IsUserAnAdmin()


# END