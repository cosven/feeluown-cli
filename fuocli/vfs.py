# -*- coding: utf-8 -*-

"""
    fuocli.vfs
    ~~~~~~~~~~

    virtual file system

"""
import os
from enum import Enum

from fuocli.exc import VfsError  # noqa


class Mode(Enum):
    """
    temporarily:

    mask: 0x0300

    **file format**
    dir: 0x0100
    file: 0x0200

    **access rights**
    other execute: 0x0001
    other write: 0x0002
    other read: 0x0004

    owner execute: 0x0008
    owner read: 0x0010
    owner write: 0x0020
    """
    mask = 0x0300
    fdir = 0x0100
    freg = 0x0200

    xusr = 0x0008
    rusr = 0x0010
    wusr = 0x0020

    xoth = 0x0001
    roth = 0x0002
    woth = 0x0004

    @classmethod
    def isdir(cls, m):
        return m & cls.mask.value == cls.fdir.value


class VfsNOENT(VfsError):
    pass


class VfsNodeExists(VfsError):
    pass


class Node(object):
    def __init__(self, name, path, mode):
        self.name = name
        self.path = path
        self.mode = mode


class Entry(Node):
    def __init__(self, name, path, parent=None):
        self.path = path
        self.name = name
        self.parent = parent
        self._childen = []
        self._node_names = set()

    def add(self, node):
        if node.name in self._node_names:
            raise VfsNodeExists
        self._node_names.add(node.name)
        self._childen.append(node)

    @property
    def nodes(self):
        return

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

    NOTE: we will eventually simulate a vfs here, however, not now -> flag

    chain(for understanding)::

        files -> files_struct(fd) -> file *[] -> file(f_dentry, f_op) ->
        dentry(d_inode) -> i_node(i_op, i_sb) -> superblock

    structure(for understanding)::

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

        self._hash_cache = dict()  # {'/Netease/xxx': 'xxx'}

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

        :return: Entry
        """
        if abspath == '/':
            return self.root

        normpath = os.path.normpath(abspath)
        entry = self._hash_cache.get(normpath)
        if entry is not None:
            return entry

        names = abspath.split('/')[1:]
        hash_cache = self._hash_cache['/']


    def get_dentry(self, dirpath):
        pass


class ProviderMountPoint(Entry):
    _instances = []

    def __init__(self, name):
        self.name = name.title()

    @classmethod
    def create(cls, name):
        return cls(name=name)


class FuoVfs(Vfs):

    def __init__(self, source):
        super().__init__()
        self.source = source

    def refresh_tree(self):
        providers = self.source.list_providers()
        for provider in providers:
            pass
