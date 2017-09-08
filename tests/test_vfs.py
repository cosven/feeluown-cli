# -*- coding: utf-8 -*-


import unittest

from fuocli.vfs import Vfs, Entry, Node


class VfsTests(unittest.TestCase):
    def test_path_lookup(self):
        vfs = Vfs()
        usr = Entry('usr', vfs.root)
        usr_bin = Entry('bin', usr)
        vfs.root.add(usr)
