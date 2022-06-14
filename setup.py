import os
from os import PathLike
from typing import Union, TypeAlias

class Types:
    StrOrBytesPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]
    FdOrAnyPath: TypeAlias = int | StrOrBytesPath

class Install:
    def __init__(self) -> None:
        pass
    
    def _change_dir(path: Types.FdOrAnyPath = ""):
        try:
            if not(os.getcwd() == path):
                os.chdir(path)
            return True
        except:
            return False
    
    def yay(self):
        pass

x = Install()
x._change_dir()
print(os.getcwd())