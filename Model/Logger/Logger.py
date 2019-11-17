from Model.Misc import Time as TIME
from Model.Database import MicroserviceDB as MD

def printLog():
    print('In logger')

class Logger:
    def __init__(self):
        self._db = MD.MicroserviceDB('TestDB.sqlite')

    def get_log_size(self):
        return self._db.get_logs_size()

    def clear(self,commit=False):
        self._db.clear_Logs(commit)

    def log_transaction(self,message,typing='TRANSACTION',commit=True):
        if not isinstance(message,str):
            raise TypeError('ERROR: Message must be of type string')

        if typing not in MD.types:
            raise ValueError('ERROR: typing must be a defined log type')

        self._db.insert_into_Logs(TIME.get_timestamp(),typing,message,commit)

    
        