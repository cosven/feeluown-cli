# -*- coding: utf-8 -*-

"""
    fuocli.vfs
    ~~~~~~~~~~

    virtual file system
"""

from fuocli.exc import VfsError  # noqa


class VfsNOENT(VfsError):
    pass


class Node(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path


class Entry(Node):
    def __init__(self, name, path, parent=None):
        self.path = path
        self.name = name
        self.parent = parent
        self._childen = []

    def add(self):
        pass

    def __contains__(self, item):
        pass


class Nameidata(object):
    """
    assistance object for path lookup
    """
    def __init__(self, dentry, name):
        self.dentry = dentry  # parent directory dentry
        self.name = name  # last component of path


class Stat(object):
    pass


class Session(object):
    def __init__(self, vfs):
        self.cwd = '/'
        self.vfs = vfs

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
        return self.cwd


class Vfs(object):
    """
    virtual file system and system call simulation

    structure::

        (root) Providers/
        ├── Netease
        │   ├── Authors
        │   │   └── ZhouJielun
        │   │       ├── Albums
        │   │       │   └── ($hash) 我很忙
        │   │       └── HotSongs
        │   └── Users
        │       ├── (~) cosven
        │       │   ├── Followers
        │       │   ├── Following
        │       │   │   └── miao -> /Netease/Users/miao/
        │       │   └── Playlists
        │       │       ├── cosven 喜欢的歌曲
        │       │       │   ├── -
        │       │       │   ├── ...
        │       │       │   └── see\ green,\ see\ blue - Jaymay
        │       │       └── $(hash) 安安静静的
        │       └── miao
        ├── Qq
        └── Xiami

    """

    def __init__(self):
        self.cwd = '/'
        self.root = Entry('/')

    def stat(self, pathname):
        """
        retrieve information about the file pointed to by pathname

        walk path and get file info from inode

        :param pathname: file or directory path, relative or absolute
        :return: Stat
        :raise VfsNOENT:
        """
        pass

    def path_lookup(self, abspath):
        """
        get nameidata of a specified pathname

        Reference: fs/namei.c -> path_lookup

        :return: Nameidata
        """
        name = abspath.split('/')[-1]
        return Nameidata(dentry, name)

    def get_dentry(self, dirpath):
        pass


class FuoVfs(Vfs):

    def __init__(self, source):
        super().__init__()
        self.source = source
