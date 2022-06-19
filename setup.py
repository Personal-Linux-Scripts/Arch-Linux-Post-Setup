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
        self.__install_list = [
            "brave-bin", 
            "spotify",
            "github-desktop-bin",
            "bitwarden",
            "firefox",
            "visual-studio-code-bin",
            "ffmpegthumbs",
            "mplayerthumbs",
            "qbittorrent",
            "teamviewer",
            "anydesk",
            "mongodb-compass",
            "virtualbox",
            "rawtherapee",
            "telegram-desktop-bin",
            "kdenlive",
            "openshot",
            "audacity",
            "handbrake",
            "stacer",
            "eclipse",
            "jdk8-openjdk",
            "pycharm-community-edition",
            "kdeconnect",
            "python",
            "python-pip",
            "python2",
            "nodejs",
            "npm",
            "tcl",
            "fpc",
            "kompozer",
            "spotiflyer-bin",
            "youtube-dl",
            "etcher",
            "shotcut",
            "notepadqq",
            "yakuake",
            "sonixd-appimage",
            "flatpak",
            "pinta",
            "photopea"
        ]   
    
    
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
    
    def _install_yay(self):
        self._change_dir()
        os.system("git clone https://aur.archlinux.org/yay.git")
        os.chdir(os.path.join(os.getcwd(), "yay"))
        os.system("makepkg -si")
        os.chdir("..")
        os.remove(os.path.join(os.getcwd(), "yay"))
    
    def packages(self):
        self._install_yay()
        os.system(
            "yay -Syy  {packages}".format(
                packages=" ".join(self.__install_list)
            )
        )


x = Install()

print(os.getcwd())
