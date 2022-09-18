import yaml

class db_settings_manager:
    
    def __init__(self):
        pass
    
    def __del__(self):
        pass

    def get_db_settings(self):
        host='127.0.0.1'
        port='3306'
        user='root'
        password='rootpass'
        database='test'
        return host, port, user, password, database

