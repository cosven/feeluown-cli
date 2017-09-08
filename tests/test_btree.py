# -*- coding: utf-8 -*-

import random
import unittest

from fuocli.btree import BTree


class BTreeTests(unittest.TestCase):
    def test_additions(self):
        bt = BTree(20)
        l = range(2000)
        for i, item in enumerate(l):
            bt.insert(item)
            self.assertEqual(list(bt), list(l[:i + 1]))

    def test_bulkloads(self):
        bt = BTree.bulkload(range(2000), 20)
        self.assertEqual(list(bt), list(range(2000)))

    def test_insert_regression(self):
        bt = BTree.bulkload(range(2000), 50)

        for i in range(100000):
            bt.insert(random.randrange(2000))
