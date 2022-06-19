#!/usr/bin/python
# -*- coding: utf-8 -*-

# This script is made for my personal computer based on my personal needs
# This script might not suite you out of the box
# but, you can customize the script easily
# Made by Hirusha Adikari ~ @hirusha-adi 

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
            "docker",
            "photopea"
        ]   
        self.__python_list = [
            "opencv-python",
            "requests",
            "flask",
            "discord",
            "uvicorn",
            "django",
            "pyinstaller"
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
    
    def main_packages(self):
        self._install_yay()
        os.system(
            "yay -Syy  {packages}".format(
                packages=" ".join(self.__install_list)
            )
        )
    
    def python_packages(self):
        os.system(
            "python -m pip install -U {packages}".format(
                packages=" ".join(self.__python_list)
            )
        )
    
    def docker_apps(self):
        
        # Install Portainer
        os.system("sudo docker volume create portainer_data")
        os.system("sudo docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:2.9.3")

        # Deemix
        os.chdir("/mnt/5D9037A9106244F3/DeemixData/docker/")
        os.system("sudo docker-compose up -d")
        
        # Navidrome
        os.chdir("/mnt/5D9037A9106244F3/NavidromeData/docker/")
        os.system("sudo docker-compose up -d")
        
if __name__ == "__main__":
    ins = Install()
    ins.main_packages()
    ins.python_packages()
    ins.docker_apps()
