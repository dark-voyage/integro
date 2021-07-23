import colorama
from colorama import Fore, Back, Style


def log(state: str, log: str):
    if state is "warning":
        print(Fore.YELLOW + Style.NORMAL + "[WARN]" + Style.RESET_ALL + " " + log)
    elif state is "info":
        pass
    pass


def init():
    colorama.init()
    pass
