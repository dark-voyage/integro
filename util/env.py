import configparser
import sys
import subprocess
from telethon import TelegramClient

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = int(config['Integro']['api_id'])
api_hash = str(config['Integro']['api_hash'])

phone = config['Account']['phone']
username = config['Account']['username']

client = TelegramClient(username, api_id, api_hash)
