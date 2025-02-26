import os
from random import choice
import string
from Transactions.Directory_Transactions import Transaction
import atexit
import time

SYS_TEMP_DIR = os.getenv('TEMP')
NAME = "FIFSOT"
CREATED_TEMP_DIR_NAME = None
CREATED_TEMP_DIR_ADDR = None
CREATED_IDS = []
ERR:bool = False

def createTempID() -> str:
    global CREATED_IDS

    TempID = "".join(choice(string.digits) for _ in range(10))

    if TempID not in CREATED_IDS:
        CREATED_IDS.append(TempID)
    
    else:
        TempID = createTempID()
    
    return TempID


def clearTemp():
    global CREATED_TEMP_DIR_ADDR

    if not isTempPrepared():
        return
    
    if not os.path.exists(CREATED_TEMP_DIR_ADDR):
        return
    
    try:
        transaction = Transaction()
        transaction.delete(obj_addr = CREATED_TEMP_DIR_ADDR,
                           only_files = False, only_content = False,
                           recursive = True, forcePermissions = True)
    
    except:
        pass


def PrepareTemp() -> None:
    global CREATED_TEMP_DIR_NAME, NAME, SYS_TEMP_DIR, CREATED_TEMP_DIR_ADDR, ERR

    # Get a new id
    tempID = createTempID()

    # Merge the name and new id
    name = "_".join([NAME, tempID])

    # Store the dir name
    CREATED_TEMP_DIR_NAME = name

    # Create temp addr
    CREATED_TEMP_DIR_ADDR = os.path.join(SYS_TEMP_DIR, CREATED_TEMP_DIR_NAME)
    
    try:
        # Create directory
        os.mkdir(CREATED_TEMP_DIR_ADDR)
    except:
        ERR = True
    else:
        ERR = False

        atexit.register(clearTemp)


def isTempPrepared() -> bool:
    global ERR

    return True if ERR == False else False


def getCreatedTempDirAddr() -> str|None:
    global CREATED_TEMP_DIR_ADDR

    if isTempPrepared():
        return CREATED_TEMP_DIR_ADDR
    
    return None


def createTempFileName(fileName:str) -> tuple[str, str]:
    """
    Gets a file name with extension and returns a tuple
    where first item is new file name with extesion and
    second item is the id itself.

    If file path is given, returns the original path head
    but with new tail.
    """
    head = os.path.split(fileName)[0]

    name, extension = os.path.splitext(fileName)

    tempID = createTempID()

    newFile = os.path.join(head, f"{tempID}{extension}")

    return newFile, tempID


def createTempAddrForTempFile(fileName:str) -> str:
    global CREATED_TEMP_DIR_ADDR
    """
    Gets a file name with extension and returns
    a temporary file address created for that file.
    """

    if not isTempPrepared():
        raise Exception("Temp directory is not set!")

    # If full address is given
    head, tail = os.path.split(fileName)

    return os.path.join(CREATED_TEMP_DIR_ADDR, tail)


def createTempDirName(dirName:str) -> tuple[str, str]:
    """
    Gets a directory name and returns a tuple where
    first item is new directory name and second item
    is the id itself.

    If directory path is given, returns the original
    path head but with new tail.
    """
    head = os.path.split(dirName)[0]

    tempID = createTempID()

    newDir = os.path.join(head, f"{dirName}_{tempID}")

    return newDir, tempID


def createTempAddrForTempDir(dirName) -> str:
    global CREATED_TEMP_DIR_ADDR
    """
    Gets a directory name and returns a temporary
    directory address created for that directory.
    """

    if not isTempPrepared():
        raise Exception("Temp directory is not set!")
    
    # If full address is given
    head, tail = os.path.split(dirName)

    return os.path.join(CREATED_TEMP_DIR_ADDR, tail)

PrepareTemp()

tempDir = createTempDirName("Resimler")
print(tempDir[0])

addr = createTempAddrForTempFile(tempDir[0])
print(addr)

time.sleep(3)