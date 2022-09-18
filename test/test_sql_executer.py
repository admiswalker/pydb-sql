import sys
import io
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import unittest
import pydb_sql.sql_executer as pydb

class Test_sql_excutor(unittest.TestCase):
    def test_connect_Ture(self):
        host='127.0.0.1'
        port='3306'
        user='root'
        password='rootpass'
        database='test'
        pd=pydb.sql_excutor()
        res = pd.connect(host, port, user, password, database) # test this line
        self.assertEqual(True, res)
        self.assertEqual(True, pd.is_connected())

    def test_connect_False(self):
        host='127.0.0.1'
        port='3306'
        user='not_existing_user'
        password='not_existing_user_pass'
        database='test'
        pd = pydb.sql_excutor()

        self.capt = io.StringIO()
        sys.stdout = self.capt
        res = pd.connect(host, port, user, password, database) # test this line
        sys.stdout = sys.__stdout__
        #print('captured: {}'.format(self.capt.getvalue()))
        
        self.assertEqual(False, res)
        self.assertEqual(False, pd.is_connected())

    def test_excute_sql(self):
        pass        

if __name__ == '__main__':
    unittest.main()
