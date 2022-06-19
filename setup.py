import os
from os import PathLike
from typing import Union, TypeAlias
from getpass import getuser

class Types:
    StrOrBytesPath: TypeAlias = str | bytes | PathLike[str] | PathLike[bytes]
    FdOrAnyPath: TypeAlias = int | StrOrBytesPath

class Install:
    def __init__(self) -> None:
        self.__HOME_FOLDER = os.path.join('/home', str(getuser()))
        self.__WORK_FOLDER = os.path.join(self.__HOME_FOLDER, 'setup')
    
    def _change_dir(self, path: Types.FdOrAnyPath = None):
        if path is None:
            path = self.__WORK_FOLDER
        try:
            if not(os.getcwd() == path):
                try:
                    os.chdir(path)
                except FileNotFoundError:
                    os.makedirs(path)
                    os.chdir(path)
            return True
        except:
            return False
    
    def yay(self):
        os.system("git clone https://aur.archlinux.org/yay.git")
        os.chdir(os.path.join(os.getcwd(), "yay"))
        os.system("makepkg -si")
        os.chdir("..")
        os.remove(os.path.join(os.getcwd(), "yay"))
    
    def others(self):
        pass    

x = Install()
x._change_dir()
x.bitwarden()

print(os.getcwd())
