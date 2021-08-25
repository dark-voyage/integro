from .logger import log
from .filename import filename
from colorama import init as colorama
from .packages import init as install
from .convert_helpers import *


def main():
    install()
    colorama()