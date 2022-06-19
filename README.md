# Arch-Linux-Post-Setup

## 1. Install Dependencies

```bash
sudo pacman -Syyu --needed base-devel python python-pip gnome-disks wget --noconfirm
```

## 2. Setup `gnome-disks` to automount drives on startup with default settings

## 3. Run script

```bash
wget "https://raw.githubusercontent.com/Personal-Linux-Scripts/Arch-Linux-Post-Setup/main/setup.py" && chmod +x ./setup.sh && python ./setup.sh
```
