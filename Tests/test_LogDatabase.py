from Model.Database import MicroserviceDB as MD
import pytest
#from mysql.connector.errors import ProgrammingError
from Model.Misc import Time as TIME


def test_MD_default_creation():
    MD.MicroserviceDB('TestDB.sqlite')

def test_MD_insert_time_failure():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    with pytest.raises(TypeError):
        logDB.insert_into_Logs('Invalid Time','TRANSACTION','This is a TEST Transaction Message')

def test_MD_insert_type_failure():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    with pytest.raises(ValueError):
        logDB.insert_into_Logs(TIME.get_timestamp(),'INVALID TYPE','This is a TEST Transaction Message')

def test_MD_insert_message_failure():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    with pytest.raises(TypeError):
        logDB.insert_into_Logs(TIME.get_timestamp(),'TRANSACTION',18)

def test_MD_insert_log():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    logDB.insert_into_Logs(TIME.get_timestamp(), 'TRANSACTION', 'This is a TEST Transaction Message')

