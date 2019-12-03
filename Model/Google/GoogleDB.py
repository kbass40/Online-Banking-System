import sys
import os
from pathlib import Path

path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')


from Model.Misc import Time as TIME

import mysql.connector

types = ['TRANSACTION','MISC','INFO']

class DatabaseConnection():
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
		self._cursor.execute("CREATE TABLE IF NOT EXISTS db.Logs(time TIMESTAMP, type VARCHAR(20), message TEXT);")
		self._cursor.execute("CREATE TABLE IF NOT EXISTS db.Stocks(gainloss DOUBLE, quantity INT);")

    
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
			raise ValueError('ERROR msg must be of type str')

		self._cursor.execute('INSERT INTO db.Logs(time, type, message) VALUES (%s, %s, %s);',(time,typ,msg))
		if commit:
			self.commit()

	def insert_into_stocks(self, gainloss: float, quantity: int, commit=True):
		if not isinstance(gainloss, float):
			raise ValueError('ERROR gainloss must be of type float')
		if not isinstance(quantity, int):
			raise ValueError('ERROR quantity must be of type int')
		self._cursor.execute('INSERT INTO db.Stocks(gainloss, quantity) VALUES (%s, %s);', (gainloss, quantity))
		if commit:
			self.commit()

	def get_logs_size(self):
		self._cursor.execute('SELECT COUNT(*) FROM db.Logs;')
		row = self._cursor.fetchone()
		return int(row[0])

	def get_stocks_size(self):
		self._cursor.execute('SELECT COUNT(*) FROM db.Stocks;')
		row = self._cursor.fetchone()
		return int(row[0])

	def clear_Logs(self, commit=False):
		self._cursor.execute('DELETE FROM db.Logs;')

		if commit:
			self.commit()

	def clear_Stocks(self, commit=False):
		self._cursor.execute('DELETE FROM db.Stocks;')

		if commit:
			self.commit()

	def get_logs(self):
		self._cursor.execute("SELECT * FROM db.Logs;")
		ret = self._cursor.fetchall()
		return ret

	def get_stocks(self):
		self._cursor.execute("SELECT * FROM db.Stocks;")
		ret = self._cursor.fetchall()
		return ret