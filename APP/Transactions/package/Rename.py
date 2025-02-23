from Transactions.package.Errors import WrongParameterError
from Transactions.package import Controller, Wrapper, Generator
import os
from os import path
import time
from typing import TypeAlias, Literal, get_args

SortType:TypeAlias = Literal["Alphabetical", "Creation Time", "Last Modification Time", "Last Access Time", "File Size"]

def rename(address:str, prefix:str = "", suffix:str = "", only_files:bool = True,
           case:SortType = "Alphabetical", rev:bool = False, start:int = 0, zfill:int = 1):
    
    if case not in get_args(SortType):
        raise WrongParameterError(msg = f"Invalid 'case' value! -> case: {case}")
    
    object_list = list()

    with os.scandir(address) as directory:
        for item in directory:
            if only_files == True and path.isdir(item.path):
                continue
            object_list.append(item.path)

    order_dict = dict()
    overlap_dict = dict()
    handled_dict = dict()
    
    if case == "Alphabetical":

        for i in range(len(object_list)):
            # Just take their names, do not include extensions
            order_dict[object_list[i]] = path.splitext(path.split(object_list[i])[1])[0]
    
    else:
        if case == "Creation Time": attribute = "st_ctime_ns"

        elif case == "Last Modification Time": attribute = "st_mtime_ns"

        elif case == "Last Access Time": attribute = "st_atime_ns"

        else: attribute = "st_size"

        for i in range(len(object_list)):
            order_dict[object_list[i]] = getattr(os.stat(object_list[i]), attribute)
    
    sorted_dict = dict(sorted(order_dict.items(), key=lambda key_val: key_val[1]))

    if rev==True: sorted_dict = dict(reversed(sorted_dict.items()))

    num = Generator.num_gen(start=start, zfill=zfill)
    
    for key, value in sorted_dict.items():
        i = next(num)
        new_name = path.join(path.split(key)[0], prefix + str(i) + suffix + path.splitext(path.split(key)[1])[1])

        if new_name in order_dict.keys() and not Controller.samefile(key, new_name):
            # By __samefile control, we avoid the following case: 0-1-2 | 2-1-0 >> 1 is not considered as a conflict
            overlap_dict[key] = new_name
            continue
        
        Wrapper.try_catch_wrapper(key, os.rename, new_name)

    for key, value in overlap_dict.items():
        if value in overlap_dict.keys() and value not in handled_dict.keys():
            head, tail = path.split(value)
            name, ext = path.splitext(tail)

            # If there is still a conflict, add the current timestamp to the name in order to make it unique
            name_tmpt = name + "_" + str(time.time())
            new_value = path.join(head, name_tmpt+ext)
            
            handled_dict[value] = new_value

            Wrapper.try_catch_wrapper(key, os.rename, new_value)
        else:
            Wrapper.try_catch_wrapper(key, os.rename, value)

    for actual_name,timestampted_name in handled_dict.items():
        Wrapper.try_catch_wrapper(timestampted_name, os.rename, actual_name)


# END