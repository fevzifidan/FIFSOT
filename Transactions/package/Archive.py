from shutil import make_archive
from typing import TypeAlias, Literal, get_args
from Transactions.package.Errors import WrongParameterError

formats:TypeAlias = Literal["zip", "tar", "gztar", "bztar", "xztar"]

def create_archive(base_name:str, format:formats, root_dir:str, base_dir:str|None = None):
    if format not in get_args(formats):
        raise WrongParameterError(msg = f"Invalid format -> format: {format}")
    
    return make_archive(base_name = base_name, format = format,
                        root_dir = root_dir, base_dir = base_dir)


# END