import sys
import io
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) # same as a below
#sys.path.append('test/..')

from pydb_sql.db_config_manager import db_config_manager as dcm

import test_config as TC

class Test_db_config_manager():

    def test_get_db_config(self):
        host, port, user, password, database = dcm.get_db_config(TC.YAML_PATH) # test this line
        
        assert(host=='127.0.0.1')
        assert(port=='3306')
        assert(user=='root')
        assert(password=='rootpass')
        assert(database=='test')

