import os,sys
from pathlib import Path

# Both parent directories need to be added to function from top-level as well as from local 
path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')
sys.path.append(str(path) + '//..//..')

from Model.Misc import Time as TIME
from Model.Database import SQLiteDatabase as SQLiteDB 

types = ['TRANSACTION','MISC','INFO']

class GoolgleDB(SQLiteDB.SQLConnection):
    def __init__(self):
        super().__init__('GoogleDB.sqlite')
        self.__setup__()

    def __setup__(self):
        self._cursor.execute("CREATE TABLE IF NOT EXISTS Logs(time TIMESTAMP, type VARCHAR(20), message TEXT);")
        self._cursor.execute("CREATE TABLE IF NOT EXISTS Stocks(gainloss DOUBLE, quantity INT);")

    def insert_into_Logs(self, time, typ, msg, commit=True):
        if not TIME.is_time_formatted(time):
            raise TypeError('ERROR time variable must be formatted in the proper format %Y-%m-%d %H:%M:?')

        if typ not in types:
            raise ValueError('ERROR typ must be one of the approved types of Logs')

        if not isinstance(msg, str):
            raise ValueError('ERROR msg must be of type str')

        self._cursor.execute('INSERT INTO Logs(time, type, message) VALUES (?, ?, ?);',(time,typ,msg))
        if commit: self.commit()

    def insert_into_stocks(self, gainloss: float, quantity: int, commit=True):
        if not isinstance(gainloss, float):
            raise ValueError('ERROR gainloss must be of type float')
        
        if not isinstance(quantity, int):
            raise ValueError('ERROR quantity must be of type int')
        
        self._cursor.execute('INSERT INTO Stocks(gainloss, quantity) VALUES (?, ?);', (gainloss, quantity))
        
        if commit: self.commit()

    def get_logs_size(self):
        self._cursor.execute('SELECT COUNT(*) FROM Logs;')
        row = self._cursor.fetchone()
        return int(row[0])

    def get_stocks_size(self):
        self._cursor.execute('SELECT COUNT(*) FROM Stocks;')
        row = self._cursor.fetchone()
        return int(row[0])

    def clear_Logs(self, commit=False):
        self._cursor.execute('DELETE FROM Logs;')

        if commit: self.commit()

    def clear_Stocks(self, commit=False):
        self._cursor.execute('DELETE FROM Stocks;')

        if commit: self.commit()

    def get_logs(self):
        self._cursor.execute("SELECT * FROM Logs;")
        ret = self._cursor.fetchall()
        return ret

    def get_stocks(self):
        self._cursor.execute("SELECT * FROM Stocks;")
        ret = self._cursor.fetchall()
        return ret
