import os
import pathlib
import util
from colorama import Fore, Back, Style


def main():
    if os.path.isfile('channels.txt'):
        util.log('warn', 'Looks like you have channels.txt which will be used by the program. Modify the file to '
                         'change your targets')
    if not os.path.isfile('channels.txt'):
        channels = []
        is_first_time = True
        save_or_no = False
        util.log('warn', 'Oh, looks like you don\'t have channels bootstrapped. Let\'s fill it together then!')
        while True:
            if is_first_time:
                channel = input(Fore.CYAN + Style.NORMAL + "[PROMPT]" + Style.RESET_ALL + " Enter the link of your "
                                                                                          "channel: ")
                if channel == "":
                    channel = input(
                        Fore.CYAN + Style.NORMAL + "[WARNING]" + Style.RESET_ALL + " You did not enter some input. "
                                                                                   "Enter the link of your channel: ")
                    channels.append(channel)
                    is_first_time = False
                else:
                    channels.append(channel)
                    is_first_time = False
            else:
                channel = input(Fore.CYAN + Style.NORMAL + "[PROMPT]" + Style.RESET_ALL + " If you want to keep going "
                                                                                          "or press [ENTER] to stop: ")
                if channel == "":
                    break
                else:
                    channels.append(channel)

        util.log('info', 'Writing all your links to text database...')
        with open('channels.txt', 'w') as file:
            for item in channels:
                file.write("%s\n" % item)
        util.log('success', 'Finished creating channels.txt')
