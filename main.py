import action
import controller
from core import client
import util

if __name__ == '__main__':
    try:
        util.main()
        controller.main()
        with client:
            client.loop.run_until_complete(action.handler())
    except Exception as error:
        print(error)
    pass
