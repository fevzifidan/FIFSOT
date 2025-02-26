from os import path
from Transactions.package.Errors import ProcessAborted

def condition_control(item:str, params:dict) -> bool:
    object_name = path.split(item)[1]
    object_extension = path.splitext(item)[1]
    
    extension, name_startswith = params["extension"], params["name_startswith"]
    contains, excl_startswith = params["contains"], params["excl_startswith"]
    excl_contains, case_insensitive = params["excl_contains"], params["case_insensitive"]

    def check_for_file():
        if extension == None or object_extension == extension:
            if name_startswith == None or object_name.startswith(name_startswith.replace("*", "")):
                if contains == None or contains.replace("*", "") in object_name:
                    if excl_startswith == None or not object_name.startswith(excl_startswith.replace("*", "")):
                        if excl_contains == None or not excl_contains.replace("*", "") in object_name:
                            return True
        return False
                        
    def check_for_dir():
        if name_startswith == None or (not name_startswith.startswith("*") and object_name.startswith(name_startswith)):
            if contains == None or (not contains.startswith("*") and contains in object_name):
                if excl_startswith == None or (not excl_startswith.startswith("*") and not object_name.startswith(excl_startswith)):
                    if excl_contains == None or (not excl_contains.startswith("*") and not excl_contains in object_name):
                        return True
        return False
    
    if case_insensitive:
        object_name = object_name.casefold()
        if name_startswith != None: name_startswith = name_startswith.casefold()
        if contains != None: contains = contains.casefold()
        if excl_startswith != None: excl_startswith = excl_startswith.casefold()
        if excl_contains != None: excl_contains = excl_contains.casefold()

    if path.isdir(item):
        return check_for_dir()
    elif path.isfile(item):
        return check_for_file()
    else:
        raise ProcessAborted(f"During condition control, Item: {item}")


# END