import tkinter
import ctypes
from tkinter import filedialog
from requests import get
import os.path

tkinter.Tk().withdraw()
MB_OK = 0x0; MB_OKCXL = 0x01; MB_YESNOCXL = 0x03; MB_YESNO = 0x04; MB_HELP = 0x4000; MB_SYSTEMMODAL = 4096; ICON_EXCLAIM = 0x30; ICON_INFO = 0x40; ICON_STOP = 0x10


def download(url, file_name):

    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)


def install():
    ctypes.windll.user32.MessageBoxW(0, u"Bitte schließ dein GTA sowie FiveM. Gib bitte dein GTA 5 Ordner an sobald du auf 'Ok' geklickt hast", u"Info", ICON_INFO)

    folder_path = filedialog.askdirectory()

    if os.path.exists(folder_path + "/GTA5.exe") and os.path.exists(folder_path + "/PlayGTAV.exe"):

        download("https://protect-v.com/share/soundfiles1.0/RESIDENT.rpf", folder_path + "/x64/audio/sfx/RESIDENT.rpf")
        download("https://protect-v.com/share/soundfiles1.0/WEAPONS_PLAYER.rpf", folder_path + "/x64/audio/sfx/WEAPONS_PLAYER.rpf")
        ctypes.windll.user32.MessageBoxW(0, u"Deine Sounds wurden geändert.", u"Erfolgreich", MB_OK)

    else:

        ctypes.windll.user32.MessageBoxW(0, u"Es konnte keine GTA5.exe sowie PlayGTAV.exe gefunden werden.", u"Error", MB_SYSTEMMODAL)


if __name__ == '__main__':
    install()
