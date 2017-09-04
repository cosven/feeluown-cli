# -*- coding: utf-8 -*-

"""
    fuocli.ctx
    ~~~~~~~~~~

    ...
"""


class AppContext(object):

    def __init__(self, vfs):
        self.cwd = '/'
        self.vfs = vfs
