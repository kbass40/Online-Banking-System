import os,sys
import sqlite3
from pathlib import Path

class SQLConnection():
    def __init__(self,db_file):
        self._conn = None
        self._cursor = None
        self.get_connection(db_file)

    def get_connection(self,db_file,new=False):
        """Creates return new Singleton database connection"""
        if new or not self._conn:
            self.__create_connection__(db_file,os.path.exists(db_file),db_file==':memory:')
            self._cursor = self._conn.cursor()
        return self._conn

    def __setup__(self):
        pass

    # Function to establish a database connection
    def __create_connection__(self,db_file,create=False,memory=False):
        if not memory:
            if create: db_file = repr(db_file)
            db_file = str(Path(__file__).parent.absolute()) + '\\'+db_file
        else: db_file = ':memory:'

        try:
            self._conn = sqlite3.connect(db_file)
            return self._conn
        except sqlite3.Error as e:
           print('ERROR:',e)
           raise e

    def commit(self):
        self._conn.commit()

   
'''# Returns a Class object based on the specified name from the database
def select_class_by_name(self,name):
    cur = self._conn._cursor()
    cur.execute("SELECT * FROM CLASSES where Name = '"+name+"';")

    results = []
    rows = cur.fetchall()
    logging.debug(rows[0])
    for i,row in enumerate(rows):
        growthRates = [(rows[i][4],rows[i][5],rows[i][6]),(rows[i][7],rows[i][8],rows[i][9]),(rows[i][10],rows[i][11],rows[i][12]),(rows[i][13],rows[i][14],rows[i][15]),(rows[i][16],rows[i][17],rows[i][18]),(rows[i][19],rows[i][20],rows[i][21])]
        unitClass = UNIT_CLASS.UnitClass(name=rows[i][0],desc=rows[i][1],maxLevel=rows[i][2],movement=rows[i][3],growthRates=growthRates)

    return unitClass
'''