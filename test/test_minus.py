import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import unittest
import pydb_sql.minus as ms

class TestMinus(unittest.TestCase):
    def test_plus_a_b(self):
        expected = -1
        actual = ms.minus_a_b(1, 2)
        self.assertEqual(expected, actual)
