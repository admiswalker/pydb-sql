import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

import unittest
import pydb_sql.pydb_sql as pydb_sql

import test_config as TC

class Test_pydb_sql():
    
    def test_connect_yaml(self):
        pds = pydb_sql.pydb_sql()
        
        tf = pds.connect_yaml(TC.YAML_PATH)
        
        assert(tf==True)
