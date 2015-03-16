import unittest
from search_n_grams import read_lines

class TestReadLinesAndComputeHashTable(unittest.TestCase):
    """
    contains test methods
    """
    def test_nowords(self):
        pass

    def test_wordsoncorners(self):
        pass

    def test_multiple4grams(self):
        pass

    def test_multiple3grams(self):
        pass

    def test_multiple2grams(self):
       pass

    def test_spaceseparators(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestReadLinesAndComputeHashTable)
unittest.TextTestRunner(verbosity=2).run(suite)