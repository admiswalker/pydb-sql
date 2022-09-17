import mysql.connector as mydb

class sql_excutor:
    
    def __init__(self):
        pass
    
    def __del__(self):
        pass

    def connect(self, host_in, port_in, user_in, password_in, database_in):
        self.conn = mydb.connect(
            host=host_in,
            port=port_in,
            user=user_in,
            password=password_in,
            database=database_in
        )
        self.conn.ping(reconnect=True)

    def is_connected(self):
        return self.conn.is_connected()

