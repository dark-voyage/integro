from util.env import *
from telethon import TelegramClient

# try:
#     from telethon import TelegramClient
# except ImportError as error:
#     print('ERROR: Oops, you forgot to install the telethon library!')
#     print('WARN: The code will install it for you')
#     subprocess.check_call([sys.executable, "-m", "pip", "install", 'telethon'])
#     pass


client = TelegramClient(username, api_id, api_hash)
