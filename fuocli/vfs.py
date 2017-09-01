# -*- coding: utf-8 -*-

"""
    fuocli.vfs
    ~~~~~~~~~~

    virtual file system
"""

from fuocli.exc import VfsError  # noqa


class VINode(object):
    pass


class Vfs(object):
    """
    virtual file system (wait, maybe not)

    - case insensitive

    virutal file system structure example::

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

    def __init__(self, source):
        self.source = source

    def listdir(self, path):
        pass

    def structure(self):
        pass
