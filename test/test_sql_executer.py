import sys
import io
import os
import traceback
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import pydb_sql.sql_executer as pydb

class Test_sql_excutor():

    def test_connect_Ture(self, capfd):
        host='127.0.0.1'
        port='3306'
        user='root'
        password='rootpass'
        database='test'
        pd=pydb.sql_excutor()
        res = pd.connect(host, port, user, password, database) # test this line
        assert(res==True)
        assert(pd.is_connected()==True) # test this line

    def test_connect_False(self, capfd):
        host='127.0.0.1'
        port='3306'
        user='not_existing_user'
        password='not_existing_user_pass'
        database='test'
        pd = pydb.sql_excutor()
        
        res = pd.connect(host, port, user, password, database) # test this line
        out, err = capfd.readouterr()
        
        assert(res==False)
        assert(pd.is_connected()==False) # test this line
        out, err = capfd.readouterr()

    def test_excute_sql(self):
        pass        

if __name__ == '__main__':
    unittest.main()
