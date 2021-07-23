
import configparser


# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = int(config['Telegram']['api_id'])
api_hash = str(config['Telegram']['api_hash'])

phone = config['Telegram']['phone']
username = config['Telegram']['username']
