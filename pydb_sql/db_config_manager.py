import yaml

class db_config_manager:
    
    @staticmethod
    def get_db_config(yml_path):
        with open(yml_path, 'r') as f:
            config = yaml.full_load(f)
        
        host = config['db_setting']['host']
        port = config['db_setting']['port']
        user = config['db_setting']['user']
        password = config['db_setting']['password']
        database = config['db_setting']['database']
        
        return host, port, user, password, database

