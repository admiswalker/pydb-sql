import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import unittest
import pydb_sql.sql_query_generator as pl

class TestPlus(unittest.TestCase):
    def test_plus_a_b(self):
        expected = 3
        actual = pl.plus_a_b(1, 2)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
