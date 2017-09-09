# -*- coding: utf-8 -*-

"""
    fuocli.ctx
    ~~~~~~~~~~

    ...
"""


class AppContext(object):

    def __init__(self, vfs, curdir):
        self.vfs = vfs
        self.curdir = curdir

    def chdir(self, pathname):
        """
        change current working directory

        :raise fuocli.vfs.VfsNOENT:
        """
        if self.vfs.stat(pathname) is not None:
            abspath = ''
            self.cwd = abspath

    def getcwd(self):
        """
        get current working directory
        """
        return self.curdir.path
