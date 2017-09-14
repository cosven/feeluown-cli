# -*- coding: utf-8 -*-

"""
    fuocli.ctx
    ~~~~~~~~~~

    ...
"""

import os

from fuocli.exc import NoSuchDir


class AppContext(object):

    def __init__(self, vfs, curdir):
        self.vfs = vfs
        self.curdir = curdir

    def chdir(self, pathname):
        """
        change current working directory

        :raise fuocli.vfs.VfsNOENT:
        """
        abspath = os.path.join(self.curdir.path, pathname)
        directory = self.vfs.path_lookup(abspath)
        if directory is None:
            raise NoSuchDir('The direcotry {} does not exist'.format(abspath))
        self.curdir = directory

    def getcwd(self):
        """
        get current working directory
        """
        return self.curdir.path
