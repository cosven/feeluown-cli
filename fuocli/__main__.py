# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import asyncio
import logging

from fuocli.app import App


handler = logging.FileHandler('fuocli.log')
formatter = logging.Formatter('%(asctime)s (%(process)d/%(threadName)s) '
                              '%(name)s %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root_logger = logging.getLogger('fuocli')
root_logger.addHandler(handler)
root_logger.setLevel(logging.DEBUG)


app = App()
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(app.run())
