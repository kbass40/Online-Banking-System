from Model.Database import LogDatabase as LD
import pytest
from mysql.connector.errors import ProgrammingError
from Model.Misc import Time as TIME

def test_LD_default_creation():
    LD.LogDatabase()

def test_LD_creation_failure():
    with pytest.raises(ProgrammingError):
        LD.LogDatabase('user','passwd')

def test_LD_insert_time_failure():
    logDB = LD.LogDatabase()
    with pytest.raises(TypeError):
        logDB.insert_into_Logs('Invalid Time','TRANSACTION','This is a TEST Transaction Message')

def test_LD_insert_type_failure():
    logDB = LD.LogDatabase()
    with pytest.raises(ValueError):
        logDB.insert_into_Logs(TIME.get_timestamp(),'INVALID TYPE','This is a TEST Transaction Message')

def test_LD_insert_message_failure():
    logDB = LD.LogDatabase()
    with pytest.raises(TypeError):
        logDB.insert_into_Logs(TIME.get_timestamp(),'TRANSACTION',18)

def test_LD_insert_log():
    logDB = LD.LogDatabase()
    logDB.insert_into_Logs(TIME.get_timestamp(), 'TRANSACTION', 'This is a TEST Transaction Message')

def test_LD_get_size():
    logDB = LD.LogDatabase()
    assert isinstance(logDB.get_size(), int) == True

def test_LD_clear_logs():
    logDB = LD.LogDatabase()
    logDB.clear_Logs()
    assert logDB.get_size() == 0