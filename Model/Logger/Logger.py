from Model.Misc import Time as TIME
from Model.Database import LogDatabase as LD

def printLog():
    print('In logger')

class Logger:
    def __init__(self):
        self._db = LD.LogDatabase()

    def get_log_size(self):
        return self._db.get_size()

    def clear(self,commit=False):
        self._db.clear_Logs(commit)

    def log_transaction(self,message,commit=True):
        if not isinstance(message,str):
            raise TypeError('ERROR: Message must be of type string')

        self._db.insert_into_Logs(TIME.get_timestamp(),'TRANSACTION',message,commit)

        