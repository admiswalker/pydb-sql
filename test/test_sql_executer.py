import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import unittest
import pydb_sql.sql_executer as pydb

class Test_sql_excutor(unittest.TestCase):
    def test_connect(self):
        host='127.0.0.1'
        port='3306'
        user='root'
        password='rootpass'
        database='test'
        pd=pydb.sql_excutor()
        pd.connect(host, port, user, password, database)
        self.assertEqual(True, pd.is_connected())

if __name__ == '__main__':
    unittest.main()
