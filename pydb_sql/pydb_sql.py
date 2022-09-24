import pydb_sql.sql_executer as pydb
from pydb_sql.db_config_manager import db_config_manager as dcm

class pydb_sql:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def test_func_plus(self, a, b):
        return a + b

    #---

    def connect(self, host, port, user, password, database):
        self.pd=pydb.sql_excutor()
        tf = self.pd.connect(host, port, user, password, database) # test this line
        
        return tf
    
    def connect_yaml(self, yaml_path):
        host, port, user, password, database = dcm.get_db_config(yaml_path)
        
        return self.connect(host, port, user, password, database)
    
    #---
    # Create

    def create_db(self):
        pass

    def create_tbl(self):
        pass

    #---
    # Read

    # db
    def db_size(self):
        pass
    
    def db_struct(self):
        pass
    
    def get_db(self):
        # return all data on the table
        pass

    # table
    def tbl_size(self):
        pass
    
    def tbl_struct(self):
        pass

    def get_tbl(self):
        # return all data on the table
        pass
    
    #---
    # Update
    
    #---
    # Delete
    
    def del_db(self):
        pass

    def del_db_data(self):
        pass

    def del_tbl(self):
        pass
    
    def del_tbl_data(self):
        pass

    #---
