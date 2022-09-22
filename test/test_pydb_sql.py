import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import unittest
import pydb_sql.pydb_sql as pydb_sql

class Test_pydb_sql(unittest.TestCase):
    def test_test_func_plus(self):
        pds = pydb_sql.pydb_sql()
        expected = 3
        actual = pds.test_func_plus(1, 2)
        self.assertEqual(expected, actual)
