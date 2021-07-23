import os
import pathlib


def main():
    input_path = input('INPUT')

    home_path = pathlib.Path.home()
    os.chdir(home_path)
    if os.path.isdir('Desktop'):
        os.chdir('Desktop')
        print('SUCCESS: Successfully entered \'Desktop\' folder')

    else:
        print('ERROR: Oh silly, looks like the folder \'Desktop\' on your Home folder doesn\'t exist. Let me create '
              'one for you...')
        os.mkdir('Desktop')
        os.chdir('Desktop')
        print('SUCCESS: Successfully entered \'Desktop\' folder')

    if os.path.isdir('Scraping'):
        os.chdir('Scraping')
        print('SUCCESS: Successfully entered \'Scraping\' folder')
    else:
        print('ERROR: Oh silly, looks like the folder \'Scraping\' on your Desktop folder doesn\'t exist. Let me '
              'create one for you...')
        os.mkdir('Scraping')
        os.chdir('Scraping')
        print('SUCCESS: Successfully entered \'Scraping\' folder')

    print("INFO: Now your current path is:", os.getcwd())

    # No need for this when Python cwd got smarter
    # os.chdir("C:/Users/a.orzikulov/Desktop/scraping")

    pass
