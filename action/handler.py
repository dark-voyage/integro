import json
import os
import re
from util import log, filename
import controller.links
from .converter import main as convert_cyrillic

async def main(client):

    if not os.path.isdir('Database'):
        log('warn', 'Seems like a folder for database outputs does not exist. Let me create it for you...')
        os.mkdir('Database')
        pass

    if not os.path.isfile('links.txt'):
        controller.links.main()

    with open('links.txt') as f:
        links = f.readlines()

    # separating links into channels and groups
    groups = []
    channels = []
    for link in links:
        search = re.search(r"[https?://]?[telegram|t]\.me(/joinchat)?/([a-zA-Z0-9_]+)", link)
        if search is not None:
            link_stripped = link.rstrip()
            if search.groups()[0] is None:
                channels.append(link_stripped)
            else:
                groups.append(link_stripped)
        else:
            log('warn', f"Sorry, the url {link_stripped} is not a valid telegram url!")

    posts = {}

    #
    # TODO: Implement private group link analyzer
    #

    if channels:
        for channel in channels:
            if channel not in posts:
                posts[channel] = {}
            try:
                entity = await client.get_input_entity(channel)
                async for message in client.iter_messages(entity, limit=100, wait_time=30):
                    post_data = (message.date, message.views, message.message)
                    posts[channel][message.id] = post_data
                log('success', f"The channel {channel} has been successfully analyzed!")
            except Exception as error:
                log('error', str(error))
                log('error', f"Could not analyze {channel}!")

        # writing to a JSON file
        try:
            os.chdir('Database')
            count = 0
            name = f"{filename(count)}.json"
            while os.path.isfile(name):
                count += 1
                name = f"{filename(count)}.json"

            with open(name, "w", encoding="UTF-8") as json_file:
                json_file.write(json.dumps(posts, indent=4, sort_keys=True, default=str))

            log('success', f"The JSON file has been created at {os.getcwd()}/{name}")
            convert_cyrillic(name)
            os.chdir('..')
        except Exception as error:
            log('error', "Error in the creation of a JSON or Excel file")
            log('error', str(error))
    else:
        log('error', 'Oh, list seems to be empty... Can\'t proceed with analyzing!')
