from colorama import Fore, Style, init
import datetime
import os
import time
import shutil
import pyfiglet


init()

c = Fore.LIGHTCYAN_EX
y = Fore.LIGHTYELLOW_EX
r = Fore.LIGHTRED_EX
re = Fore.RESET

dim = Style.DIM
res = Style.RESET_ALL


total_time = 0


def start():
    text = pyfiglet.figlet_format("UPDATE")

    print(text)



def totime(seconds):
    # Get a time structure representing the duration
    time_struct = time.gmtime(seconds)

    # Format the time structure as HH:MM:SS
    formatted_time = time.strftime("%Hh %Mm %Ss", time_struct)

    return formatted_time


def update(command, type):
    global total_time

    print("")

    try:
        terminal_size = shutil.get_terminal_size()
        columns = terminal_size.columns

        line = "-"*columns

        print(f"{dim}{line}{res}")

    except OSError:
        pass

    print("")

    print(f"{c}[*]{re} Type: {c}{type}{re}")
    print(f"{c}[*]{re} Command: {c}{command}{re}")
    print("")

    ask = input(f"{y}[+] Run command? {dim}[Y|n]:{res} ")

    print("")

    if ask == "" or ask == "Y" or ask == "y":
        start = datetime.datetime.now()

        os.system(command)

        end = datetime.datetime.now()

        difference = end - start

        print("")
        print(f"{c}[*]{re} Duration: {totime(difference.seconds)}")

        total_time += difference.seconds


def totaltime():
    global total_time

    print("")
    print(f"{c}[*]{re} Total: {totime(total_time)}")



start()
update("sudo pacman -Syu", "PACMAN")
update("yay -Sua", "YAY")
update("sudo flatpak update", "FLATPAK")
totaltime()
