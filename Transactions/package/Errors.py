"""
pass
"""

from typing import TypeAlias, Literal, get_args

AdminErrorCase:TypeAlias = Literal["copy_symlink", "create_symlink", "terminate_process"]

ERRCODE:dict[str,str] = dict()

ERRCODE = {
    "SymLinkCycle"              :   "Symlink cycle has occurred!",
    "SpecialFile"               :   "Special file encountered!",
    "NestedSymLink"             :   "Creating another symlink within a symlink is not allowed!",
    "UnidentifiedSpecialFile"   :   "Unidentified special file encountered!",
    "LoopError"                 :   "File-system loop has occurred!"
}

class SourceNotFoundError(Exception):
    """Raised when source is not found"""

    def __init__(self, address = "Not specifically stated!"):
        self.message = f"The source address that you have given was not found! >> {address}"
        super().__init__(self.message)

class SameFileError(Exception):
    """Raised when source and destination are the same file."""
    
    def __init__(self, src, dest):
        self.message = f"Source and Destination cannot point to the same address! >> Source: {src} -- Destination: {dest}"
        super().__init__(self.message)

class SpecialFileError(Exception):
    """
    Raised when trying to do a kind of operation (e.g. copying) which is
    not supported on a special file (e.g. a named pipe)
    """
    
    def __init__(self, address = "Not specifically stated!"):
        self.message = f"We encountered a kind of special file! >> {address}"
        super().__init__(self.message)

class UnidentifiedSpecialFile(Exception):
    """
    Raised when trying to do a kind of operation (e.g. copying) which is
    not supported on an unidentified special file (e.g. a named pipe)
    """
    
    def __init__(self, address = "Not specifically stated!"):
        self.message = f"We encountered a kind of unidentified special file! >> {address}"
        super().__init__(self.message)

class NotASymlinkError(Exception):
    """Raised when a non-symlink is given to 'symlink_deleter'"""
    
    def __init__(self, address = "Not specifically stated!"):
        self.message = f"The object address you gave is not a symlink! >> {address}"
        super().__init__(self.message)

class InSymlinkError(Exception):
    """Raised when a file or directory is in symlink"""

    def __init__(self, obj_address, func):
        self.message = f"""It is being tried to perform a - {func} - operation on an object which is in a symlink.
        Please check the 'in_symlink_ok' parameter! >> {obj_address}"""

        super().__init__(self.message)

class NotAnAdminError(Exception):
    """Raised when an operation that requires admin authority tried to be
    performed without admin authority"""

    def __init__(self, case:AdminErrorCase=None):
        if case == None or case not in get_args(AdminErrorCase):
            self.message = "Unexplained error condition about the requirement of administrator privileges!"
        elif case == "copy_symlink":
            self.message = "Copying symlinks requires administrator privileges."\
                            "Check 'symlinks' parameter or run the script as administrator."
        elif case == "create_symlink":
            self.message = "Creating symlinks requires administrator privileges."\
                            "You can try to run the script as administrator."
        elif case == "terminate_process":
            self.message = "Terminating a running process (not recommended) requires administrator privileges."\
                            "You can try to run the script as administrator."
        else: pass
        
        super().__init__(self.message)

class CompletedProcessWithMissingItems(Exception):
    """Raised when a transaction is done with missing files or items. Check 'errors' dictionary."""

    def __init__(self, arg):
        self.message = f"Process completed with missing items. Missing items were let be. {arg}"

        super().__init__(self.message)

class ProcessAborted(Exception):
    """If something crucial occurs, the entire process is
    aborted with this error in order to avoid further errors."""

    def __init__(self, *args):
        err_info = args[0]
        for arg in args[1:]:
            err_info += " -- " + arg
        self.message = f"""Process aborted! >> Error related information: {err_info}"""

        super().__init__(self.message)

class WrongParameterError(Exception):
    """
    Raised when a function gets an invalid parameter.
    """

    def __init__(self, addtInfo:str|None = None, msg:str|None = None):
        defaultMsg = "Function failed due to a wrong parameter!"

        if addtInfo == None and msg == None:
            self.msg = defaultMsg

        elif addtInfo != None and msg != None:
            self.msg = f"{msg} | {addtInfo}"
        
        elif addtInfo != None and msg == None:
            self.msg = f"{defaultMsg} | {addtInfo}"

        elif addtInfo == None and msg != None:
            self.msg = msg

        super().__init__(self.msg)

class NestedSymlinkError(Exception):
    """
    Raised when a symlink is tried to be created in another symlink
    """

    def __init__(self, addr:str|None = None):
        if addr == None: addr = ""
        else: addr = f"| {addr}"
        self.message = f"Creating another symlink within a symlink is not allowed! {addr}"

        super().__init__(self.message)

class SelfOverWrittenError(Exception):
    """
    Raised when a file/folder is tried to be written on itself.
    """

    def __init__(self, addt_info:str|None = None):
        if addt_info == None: addt_info = ""
        else: addt_info = f"| {addt_info}"
        self.message = f"Self-overwritten is not allowed! {addt_info}"

        super().__init__(self.message)

class LoopError(Exception):
    """
    Raised when it is detected that source and destination configuration
    have a potential to create an infinite-loop in file system.
    """

    def __init__(self, addt_info:str|None = None):
        if addt_info == None: addt_info = ""
        else: addt_info = f"| {addt_info}"
        self.message = f"A file-system loop has occurred! {addt_info}"

        super().__init__(self.message)

class UnsuitablePathError(Exception):
    """
    Raised when the given path(s) is not rooted or contains navigational references.
    """

    def __init__(self, addt_info:str|None = None):
        if addt_info == None: addt_info = ""
        else: addt_info = f"| {addt_info}"
        self.message = f"Given path(s) not suitable! {addt_info}"

        super().__init__(self.message)

class WinErrors:
    errors:dict[int,str] = dict()

    errors = {
        4       :   False,
        5       :   True,
        7       :   False,
        14      :   False,
        16      :   True,
        32      :   True,
        33      :   True,
        39      :   False,
        145     :   True,
        220     :   True,
        225     :   False,
        226     :   True,
        303     :   True,
        313     :   False,
        334     :   False,
        336     :   False,  #   XXX
        337     :   True,
        754     :   True,
        995     :   False,  #   XXX
        1117    :   False,
        1296    :   True,   #   XXX
        1314    :   True,
        1392    :   True,
        1920    :   True,

    }


# END