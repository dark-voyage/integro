import configparser
import sys
import subprocess

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = int(config['Integro']['api_id'])
api_hash = str(config['Integro']['api_hash'])

phone = config['Account']['phone']
username = config['Account']['username']


try:
    from telethon import TelegramClient
except ImportError as error:
    print('ERROR: Oops, you forgot to install the telethon library!')
    print('WARN: The code will install it for you')
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'telethon'])
    from telethon import TelegramClient
    pass

client = TelegramClient(username, api_id, api_hash)
