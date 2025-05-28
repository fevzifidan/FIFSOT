from os import path

def condition_control(item:str, params:dict) -> bool:
    object_name = path.split(item)[1]
    object_extension = path.splitext(item)[1]
    
    extension, name_startswith = params["extension"], params["name_startswith"]
    contains, excl_startswith = params["contains"], params["excl_startswith"]
    excl_contains, case_insensitive = params["excl_contains"], params["case_insensitive"]

    if case_insensitive:
        object_name = object_name.casefold()
        if name_startswith != None: name_startswith = name_startswith.casefold()
        if contains != None: contains = contains.casefold()
        if excl_startswith != None: excl_startswith = excl_startswith.casefold()
        if excl_contains != None: excl_contains = excl_contains.casefold()

    if path.isfile(item):
        if extension != None and object_extension != extension:
            return False
    
    if params["filterOnlyForFiles"]: return True
    
    if name_startswith != None and not object_name.startswith(name_startswith):
        return False
    
    elif contains != None and not contains in object_name:
        return False
    
    elif excl_startswith != None and object_name.startswith(excl_startswith):
        return False
    
    elif excl_contains != None and excl_contains in object_name:
        return False
    
    else:
        return True


# END