# -*- coding: utf-8 -*-


import unittest

from fuocli.vfs import Vfs, Entry, Node, ENTRY_DEFAULT_MODE


class VfsTests(unittest.TestCase):
    def test_path_lookup(self):
        vfs = Vfs()
        usr = vfs.create('usr', vfs.root, mode=ENTRY_DEFAULT_MODE)
        usr_bin = vfs.create('bin', usr, mode=ENTRY_DEFAULT_MODE)
        entry = vfs.path_lookup('/usr/bin')
        self.assertEqual(entry, usr_bin)

        entry = vfs.path_lookup('/usr/bin/hello')
        self.assertEqual(entry, None)

        vim = vfs.create('vim', usr_bin)
        entry = vfs.path_lookup('/usr/bin/vim')
        self.assertEqual(entry, vim)
