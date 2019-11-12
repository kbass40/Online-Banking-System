# Class defines the abstract database interface our app communes with
import mysql.connector
from Model.Misc import Time as TIME

types = ['TRANSACTION','MISC','INFO']

class LogDatabase():
    def __init__(self, user='user',password='password'):
        self._conn = mysql.connector.connect(
                host="localhost",
                user=user,
                passwd=password,
                db="db"
            )
        self._cursor = self._conn.cursor()
        self.__initialize__()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    def __initialize__(self):
        self._cursor.execute("CREATE TABLE IF NOT EXISTS db.Logs(time TIMESTAMP, type VARCHAR(20), message TEXT, time);")

    
    @property
    def connection(self):
        return self._conn
    
    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def insert_into_Logs(self, time, typ, msg, commit = True):
        if not TIME.is_time_formatted(time):
            raise TypeError('ERROR time variable must be formatted in the proper format %Y-%m-%d %H:%M:%S')

        if typ not in types:
            raise ValueError('ERROR typ must be one of the approved types of Logs')

        if not isinstance(msg, str):
            raise TypeError('ERROR msg must be of type str')

        self._cursor.execute('INSERT INTO db.Logs(time, type, message) VALUES (%s, %s, %s);',(time,typ,msg))
        if commit:
            self.commit()

    def get_size(self):
        self._cursor.execute('SELECT COUNT(*) FROM db.Logs;')
        row = self._cursor.fetchone()
        return int(row[0])

    def clear_Logs(self, commit=False):
        self._cursor.execute('DELETE FROM db.Logs;')

        if commit:
            self.commit()
    