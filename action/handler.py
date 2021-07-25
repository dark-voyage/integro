import json
import os
import re
from util import log, filename
import controller.links
from transliterate import translit


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
            # util.log('success', f"Congrats, the url {link.rstrip()} is valid!")
            username = search.groups()[1]
            if search.groups()[0] is None:
                channels.append(f"https://t.me/{username}")
            else:
                groups.append(f"https://t.me/joinchat/{username}")
        else:
            log('warn', f"Sorry, the url {link.rstrip()} is not a valid telegram url!")

    posts = {}

    #
    # TODO: Implement private group link analyzer (due: in a day [today] || in 2 days @genemator)
    #

    if channels:
        for channel in channels:
            if channel not in posts:
                posts[channel] = {}
            try:
                async for message in client.iter_messages(channel, limit=2):
                    posts[channel][message.id] = translit(u"" + message.message, 'uz')
            except Exception as error:
                log('error', str(error))
            log('success', f"The channel {channel.rstrip()} has been successfully analyzed!")

        # writing to a JSON file
        try:
            os.chdir('Database')
            count = 0
            while True:
                if os.path.isfile(f"{filename(count)}.json"):
                    count += 1
                if not os.path.isfile(f"{filename(count)}.json"):
                    name = filename(count)
                    break

            with open(f"{name}.json", "w", encoding="UTF-8") as json_file:
                json_file.write(json.dumps(posts, indent=4, sort_keys=True))

            log('success', f"The JSON file has been created successfully as {os.getcwd()}/{name}.json")
            os.chdir('..')
        except Exception as error:
            log('error', f"Could not create the JSON file")
            log('error', str(error))
    else:
        log('error', 'Oh, list seems to be empty... Can\'t proceed with analyzing!')

    await client.disconnected
