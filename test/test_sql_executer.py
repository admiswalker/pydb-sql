import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import io
from pydb_sql.db_config_manager import db_config_manager as dcm
import test_config as TC

import pydb_sql.sql_executer as pydb


class Test_sql_excutor():

    def test_connect_Ture(self, capfd):
        host, port, user, password, database = dcm.get_db_config(TC.YAML_PATH)
        
        pd=pydb.sql_excutor()
        tf = pd.connect(host, port, user, password, database) # test this line
        
        assert(tf==True)
        assert(pd.is_connected()==True) # test this line

    def test_connect_False(self, capfd):
        host, port, user, password, database = dcm.get_db_config(TC.YAML_PATH)
        user='not_existing_user'
        password='not_existing_user_pass'
        
        pd = pydb.sql_excutor()
        tf = pd.connect(host, port, user, password, database) # test this line
        out, err = capfd.readouterr()
        assert(tf==False)
        
        assert(pd.is_connected()==False) # test this line
        out, err = capfd.readouterr()

    def test_excute_sql_S(self):
        host, port, user, password, database = dcm.get_db_config(TC.YAML_PATH)
        
        pd=pydb.sql_excutor()
        pd.connect(host, port, user, password, database) # test this line
        tf, ret = pd.excute(query='show databases;')
        assert(tf==True)
        #assert(ret.find('information_schema'))
        #assert(ret.find('mysql'))
        #assert(ret.find('performance_schema'))
        #assert(ret.find('sys'))
        
        print(tf)
        print(ret)
        print(type(ret))
        print(type(ret[0]))

