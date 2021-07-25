import sys
import subprocess

from .logger import log


def init():
    try:
        from telethon import TelegramClient
        from transliterate import translit
        from colorama import init
    except ImportError as error:
        log('error', f"Oops, you forgot to install the {error.name}!")
        log('warn', f"The program will install it for you")
        subprocess.check_call([sys.executable, "-m", "pip", "install", error.name])
        pass
