import yaml

class db_config_manager:
    
    @staticmethod
    def get_db_config(yml_path):
        with open(yml_path, 'r') as f:
            config = yaml.full_load(f)
        
        print(config)
        #host='127.0.0.1'
        #port='3306'
        #user='root'
        #password='rootpass'
        #database='test'
        #return host, port, user, password, database

