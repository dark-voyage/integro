import controller
import action
# import asyncio
import connector
import util


if __name__ == '__main__':
    try:
        util.main()
        controller.main()
        with connector.client as client:
            client.loop.run_until_complete(action.handler(client))

            # loop = asyncio.get_event_loop()
            # loop.run_until_complete(action.handler(client))

    except Exception as error:
        print(str(error))
    pass
