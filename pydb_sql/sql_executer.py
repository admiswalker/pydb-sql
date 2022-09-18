import mysql.connector as mydb

class sql_excutor:
    
    def __init__(self):
        pass
    
    def __del__(self):
        pass

    def connect(self, host_in, port_in, user_in, password_in, database_in):
        try:
            self.conn = mydb.connect(
                host=host_in,
                port=port_in,
                user=user_in,
                password=password_in,
                database=database_in
            )
        except Exception as err:
            print('sql_excutor: connect() is failed:', err)
            return False
        
        self.conn.ping(reconnect=True)
        return True

    def is_connected(self):
        try:
            res = self.conn.is_connected()
        except Exception as err:
            print('sql_excutor: is_connected() is failed:', err)
            return False
        
        return res

    def excute(self, query):
        cur = self.conn.cursor()
        
        try:
            cur.execute(query)
            res = cur.fetchall()
        except Exception as e:
            print('[Table Create Error]', e)
            return False, res
        
        return True, res

