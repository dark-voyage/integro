import json
import csv
# import getpass
import os

import controller.channels
import util
from core import client


async def main():
    #
    # In case of two factor key activated
    # => but not sure whether does it work or not ;)
    #

    # try:
    #     await client.sign_in(code=input('Enter code: '))
    # except SessionPasswordNeededError:
    #     await client.sign_in(password=getpass.getpass())

    if not os.path.isdir('CSV'):
        util.log('warn', 'Seems like a folder for CSV outputs does not exist. Let me create it for you...')
        os.mkdir('CSV')
        pass

    if not os.path.isdir('JSON'):
        util.log('warn', 'Seems like a folder for JSON outputs does not exist. Let me create it for you...')
        os.mkdir('JSON')
        pass

    #
    # Notice!
    # channels.txt file should be located at the 'Scraping' folder on your desktop
    # TODO: Write an automation for channels listing (due tomorrow: genemator)
    #

    if not os.path.isfile('channels.txt'):
        controller.channels.main()

    with open('channels.txt') as f:
        channels = f.readlines()

    #
    # All links in channels.txt should be seperated by a new line
    # Expected parsed file results:
    # [ 'https://t.me/example', 'https://t.me/example' ]
    #

    for channel in channels:
        name = (await client.get_entity(channel)).title.replace('|', '-')
        posts = {}

        async for message in client.iter_messages(channel, limit=200):
            posts[message.id] = message.text

        filename = f"{name} {list(posts.keys())[0]}-{list(posts.keys())[-1]}"

        #
        # It will create JSON and CSV folder for each kind of data type
        #

        try:
            os.chdir('CSV')
            with open(f"{filename}.csv", 'w', encoding="UTF-32") as csv_file:
                writer = csv.writer(csv_file)
                for key, value in posts.items():
                    writer.writerow([key, value])
                pass
            pass
            util.log('success', f"The CSV file has been created successfully for {name} channel")
            os.chdir('..')
        except Exception as error:
            util.log('error', f"Could not create the csv file of {name} channel")
            pass

        try:
            os.chdir('JSON')
            with open(f"{filename}.json", "w", encoding="UTF-8") as json_file:
                # This one writes pretty json
                json_file.write(json.dumps(posts, indent=4, sort_keys=True))

                # This one doesn't
                # json.dump(post_dict, json_file)
            pass
            util.log('success', f"The JSON file has been created successfully for {name} channel")
            os.chdir('..')
        except Exception as error:
            util.log('error', f"Could not create the JSON file of {name} channel")
