import psutil
from os import path
from Transactions.package import Controller


def detectFileHolder(file_path:str|list) -> dict[str,tuple[str,int]]|None:
    """
    tuple: (process:str, pid:int)
    """

    if isinstance(file_path, str):
        file_path = [file_path,]
    
    # Define a dict that matches paths with processes
    match_dict = dict()
    
    # Define an index variable to loop through the list
    index = 0
    while True:
        try:
            file = file_path[index]
            if not path.exists(file):
                file_path.pop(index)
            else:
                index += 1
        except IndexError:
            break
    
    if len(file_path) == 0:
        return None
    
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            open_files = proc.info['open_files']
            if open_files:
                for file in open_files:
                    if Controller.getNormalizedPath(file.path) in file_path:
                        match_dict[file.path] = (proc.info['name'], proc.info['pid'])
                        
                        # Once obtain the desired processes, do not go further
                        if len(match_dict) >= len(file_path):
                            return match_dict
                        
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    return match_dict


def isPIDValid(pid:int) -> bool:
    return psutil.pid_exists(pid)


def getOpenFilesFromPID(pid:int):
    """
    Returns open files that the process with given pid
    holds
    """

    try:

        openFiles = psutil.Process(pid).open_files()

        return openFiles
    
    except Exception as e:
        print(str(e))
        return None


def checkFilePIDMatch(pid:int, file_path:str):
    if not isPIDValid(pid):
        return False
    
    file_path = path.normpath(file_path)
    
    openFiles = getOpenFilesFromPID(pid)

    if openFiles:
        for file in openFiles:
            if path.normpath(file.path) == file_path:
                return True
        
        return False
    
    return False


def terminateProcess(pid:int) -> bool:
    """
    Returns True if termination is successful, False otherwise.
    """

    if not isPIDValid(pid):
        return False

    try:    
        process = psutil.Process(pid)
        process.terminate()
    
    except Exception as e:
        return False
    
    else:
        return True


# END