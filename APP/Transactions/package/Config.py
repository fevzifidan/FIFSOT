import shutil
from Transactions.package.Counter import count

COND = {"extension":None, "name_startswith":None, "contains":None,
        "excl_startswith":None, "excl_contains":None, "case_insensitive":False}

ERRORS = dict()

ERROR_PATHS = list()

DIRECTORY_TO_LEAVE_ADDRESS = ""

MAX_OPERATION_LIMIT = 0

COPY_FUNCTION = shutil.copy2

FORCE_PERMISSIONS = True


def setMaxOperationLimit(*paths):
    global MAX_OPERATION_LIMIT
    
    # XXX If the caller is a delete function, +1 additional operation right is granted. XXX
    # XXX If the caller is a copy function, double operation right is granted. XXX
    MAX_OPERATION_LIMIT = 0

    for path in paths:
        MAX_OPERATION_LIMIT += count(path, only_files=False, recursive=True, follow_symlinks=True)

    MAX_OPERATION_LIMIT *= 2
    
    # If an empty directory is given, for example, its count value will be 0.
    # If it stays as 0, then given directory cannot be deleted or copied.
    # Set it to 1.
    if MAX_OPERATION_LIMIT == 0:
        MAX_OPERATION_LIMIT = 1


def addError(errCode, *paths):
    global ERRORS
    
    ERRORS[errCode] = ERRORS.get(errCode, 0) + 1

    for path in paths:
        ERROR_PATHS.append(path)


# END