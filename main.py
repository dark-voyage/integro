import controller
from action import get_posts
import connector
import util


if __name__ == '__main__':
    try:
        util.main()
        controller.main()
        with connector.client as client:
            client.loop.run_until_complete(get_posts(client))          

    except Exception as error:
        util.log("error", str(error))
