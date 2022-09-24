import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import unittest
import pydb_sql.pydb_sql as pydb_sql

import test_config as TC

class Test_pydb_sql():
    
    def test_connect_yaml_S(self):
        pds = pydb_sql.pydb_sql()
        tf = pds.connect_yaml(TC.YAML_PATH) # test this line
        assert(tf==True)
        
    #---
    # Create
    
    def test_create_db(self):
        pds = pydb_sql.pydb_sql()
        pds.connect_yaml(TC.YAML_PATH)
        
        db_name="TEST_DB"
        tf, ret = pds.create_db(db_name) # test this line
        assert(tf==True)
        
        tf, ret = pds.db_all()
        assert(tf==True)
        assert(len(ret)==6)
        assert(db_name in ret)
        
        tf, ret = pds.rm_db(db_name)
        assert(tf==True)

    #---
    # Read
    
    def test_db_all(self):
        pds = pydb_sql.pydb_sql()
        pds.connect_yaml(TC.YAML_PATH)
        
        tf, ret = pds.db_all()
        assert(tf==True)
        assert(ret==['information_schema', 'mysql', 'performance_schema', 'sys', 'test'])

    #---
    # Delete
    
    def test_rm_db(self):
        pds = pydb_sql.pydb_sql()
        pds.connect_yaml(TC.YAML_PATH)
        
        db_name="TEST_DB"
        tf, ret = pds.create_db(db_name)
        assert(tf==True)
        
        tf, ret = pds.rm_db(db_name) # test this line
        assert(tf==True)
        
        tf, ret = pds.db_all()
        assert(tf==True)
        assert(len(ret)==5)
        assert(db_name not in ret)

