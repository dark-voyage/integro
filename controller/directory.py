import os
import pathlib
import util


def main():
    # input_path = input('INPUT')

    home_path = pathlib.Path.home()
    os.chdir(home_path)
    if os.path.isdir('Desktop'):
        os.chdir('Desktop')
        util.log('success', 'Successfully entered \'Desktop\' folder')

    else:
        util.log('error', 'Oh silly, looks like the folder \'Desktop\' on your Home folder doesn\'t exist. Let me '
                          'create one for you...')
        os.mkdir('Desktop')
        os.chdir('Desktop')
        util.log('success', 'Successfully entered \'Desktop\' folder')

    if os.path.isdir('Scraping'):
        os.chdir('Scraping')
        util.log('success', 'Successfully entered \'Scraping\' folder')
    else:
        util.log('error', 'Oh silly, looks like the folder \'Scraping\' on your Desktop folder doesn\'t exist. Let me '
                          'create one for you...')
        os.mkdir('Scraping')
        os.chdir('Scraping')
        util.log('success', 'Successfully entered \'Scraping\' folder')

    util.log('info', "Now your current path is: " + os.getcwd())
