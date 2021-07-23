import controller
import middleware
from core import client
import util

if __name__ == '__main__':
    try:
        util.main()
        controller.main()
        util.log('')
        # with client:
        #     client.loop.run_until_complete(middleware.main())
    except Exception as error:
        print(error)
    pass
