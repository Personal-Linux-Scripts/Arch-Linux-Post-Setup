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
    
    def visual_studio_code(self):
        os.system("yay -S visual-studio-code-bin")
    
    def vscodium(self):
        os.system("yay -S vscodium-bin")
    
    def brave_browser(self):
        os.system("yay -S brave-bin")
    
    def github_desktop(self):
        os.system("yay -S github-desktop-bin")
    
    def mongodb_compass(self):
        os.system("yay -S mongodb-compass")
    
    def discord(self):
        os.system("yay -S discord")
    
    def fish(self):
        os.system("yay -S fish")
        
    def zsh(self):
        os.system("yay -S zsh")
    
    def bitwarden(self):
        os.system("yay -S bitwarden")
    

x = Install()
x._change_dir()
x.bitwarden()

print(os.getcwd())
