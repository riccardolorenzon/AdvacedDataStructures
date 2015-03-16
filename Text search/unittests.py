import unittest
from search_n_grams import read_lines

class TestReadLinesAndComputeHashTable(unittest.TestCase):
    """
    contains test methods
    """
    def test_nowords(self):
        lines = ['']
        hash_table = dict()
        read_lines(lines, hash_table)
        self.assertEqual(len(hash_table.keys()),0)

    def test_wordsoncorners(self):
        lines = ['a b c d e', 'a f g h e', 'e a b g d g h h']
        hash_table = dict()
        read_lines(lines, hash_table)
        self.assertEqual(hash_table['e a'], [2,2])

    def test_multiple4grams(self):
        lines = ['a b c d e', 'a c g h e', 'e d e a c g h h']
        hash_table = dict()
        read_lines(lines, hash_table)
        self.assertEqual(hash_table['d e a c'], [4,2])

    def test_multiple3grams(self):
        lines = ['a b c d e', 'a j k h e', 'e e a j c g h h']
        hash_table = dict()
        read_lines(lines, hash_table)
        self.assertEqual(hash_table['e a j'], [3,2])

    def test_multiple2grams(self):
        lines = ['a b c d e', 'b c k h b', 'c e a j c g h h']
        hash_table = dict()
        read_lines(lines, hash_table)
        self.assertEqual(hash_table['b c'], [2,3])

    def test_spaceseparators(self):
        lines = ['a b c abc cd c', 'd a b c ab', 'c c ac d']
        hash_table = dict()
        read_lines(lines, hash_table)
        self.assertEqual(hash_table['a b c'], [3,2])
        self.assertEqual(hash_table['ab c'], [2,1])

suite = unittest.TestLoader().loadTestsFromTestCase(TestReadLinesAndComputeHashTable)
unittest.TextTestRunner(verbosity=2).run(suite)