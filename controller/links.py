import os
import util
from colorama import Fore, Back, Style


def main():
    if os.path.isfile('links.txt'):
        util.log('info', 'You have link.txt, which will be used by the program.')

    if not os.path.isfile('links.txt'):
        links, link = [], ""
        is_first_time, is_first_failed = True, False
        util.log('warn', 'Oh, looks like you don\'t have channels and groups file bootstrapped. Let\'s fill it together'
                         ' then!')
        while True:
            if is_first_time and not is_first_failed:
                link = input(Fore.CYAN + Style.NORMAL + "[PROMPT]" + Style.RESET_ALL + " Enter the link of your "
                                                                                       "channel | group: ")
            if not is_first_time and not is_first_failed:
                link = input(Fore.CYAN + Style.NORMAL + "[PROMPT]" + Style.RESET_ALL + " If you want to keep going "
                                                                                       "or press [ENTER] to stop: ")
            if (is_first_time and is_first_failed) or (not is_first_time and is_first_failed):
                link = input(
                    Fore.YELLOW + Style.NORMAL + "[WARNING]" + Style.RESET_ALL + " You did not enter some input. "
                                                                                 "Enter the link of your channel | "
                                                                                 "group: ")

            if link == "" or link == " ":
                if is_first_time:
                    is_first_failed = True
                else:
                    break
            else:
                if is_first_failed:
                    links.append(link)
                    is_first_time = False
                    is_first_failed = False
                else:
                    links.append(link)

        util.log('info', 'Writing all your links to text database...')
        with open('links.txt', 'w') as file:
            for item in links:
                file.write("%s\n" % item)
        util.log('success', 'Finished creating links.txt')
