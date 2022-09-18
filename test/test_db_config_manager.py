import sys
import io
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import pydb_sql.db_config_manager as dcm

class Test_db_config_manager():

    def test_connect_False(self, capfd):
        dcm.get_db_config()
        out, err = capfd.readouterr()
        print(out)
        print(err)
        '''
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
        '''

    def test_excute_sql(self):
        pass

