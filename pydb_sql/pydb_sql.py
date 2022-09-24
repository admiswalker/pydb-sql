import pydb_sql.sql_executer as pydb
from pydb_sql.db_config_manager import db_config_manager as dcm
import pydb_sql.type_conversion as cnv

class pydb_sql:
    def __init__(self):
        self.pd=''

    def __del__(self):
        pass

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

    def create_db(self, db_name):
        sql_query = 'create database '+db_name
        tf, ret = self.pd.excute(sql_query)
        return tf, ret

    def create_tbl(self):
        pass

    #---
    # Read

    # db
    def db_all(self):
        # return all data on the server
        
        sql_query = 'show databases;'
        tf, ret = self.pd.excute(sql_query) # test this line
        if tf==False:
            return tf, ret
        
        ret = cnv.LT2L(ret)
        
        return tf, ret

    def db_size(self):
        pass
    
    def db_struct(self):
        pass
    
    # table
    def tbl_all(self):
        # return all data on the table
        pass
    
    def tbl_size(self):
        pass
    
    def tbl_struct(self):
        pass

    #---
    # Update
    
    #---
    # Delete
    
    def rm_db(self, db_name):
        sql_query = 'drop database '+db_name
        tf, ret = self.pd.excute(sql_query)
        return tf, ret

    def rm_db_data(self):
        pass

    def rm_tbl(self):
        pass
    
    def rm_tbl_data(self):
        pass

    #---
