from Model.Database import MicroserviceDB as MD
import pytest
#from mysql.connector.errors import ProgrammingError
from Model.Misc import Time as TIME

<<<<<<< HEAD
<<<<<<< HEAD
def test_MD_default_creation():
    MD.MicroserviceDB('TestDB.sqlite')

=======

=======
>>>>>>> Added back get_size and clear_log tests, and xfail
def test_MD_default_creation():
    MD.MicroserviceDB('TestDB.sqlite')

>>>>>>> Rewrote test_LogDatabase to fit SQLlite queries
def test_MD_insert_time_failure():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    with pytest.raises(TypeError):
        logDB.insert_into_Logs('Invalid Time','TRANSACTION','This is a TEST Transaction Message')

def test_MD_insert_type_failure():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    with pytest.raises(ValueError):
        logDB.insert_into_Logs(TIME.get_timestamp(),'INVALID TYPE','This is a TEST Transaction Message')

<<<<<<< HEAD
<<<<<<< HEAD
=======
def test_MD_insert_message_failure():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    with pytest.raises(TypeError):
        logDB.insert_into_Logs(TIME.get_timestamp(),'TRANSACTION',18)

>>>>>>> Rewrote test_LogDatabase to fit SQLlite queries
=======
>>>>>>> Added back get_size and clear_log tests, and xfail
def test_MD_insert_log():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    logDB.insert_into_Logs(TIME.get_timestamp(), 'TRANSACTION', 'This is a TEST Transaction Message')

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> Added back get_size and clear_log tests, and xfail
def test_LD_get_size():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    assert isinstance(logDB.get_logs_size(), int) == True

def test_LD_clear_logs():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    logDB.clear_Logs()
    assert logDB.get_logs_size() == 0

<<<<<<< HEAD
#This test is supposed to fail
=======
>>>>>>> Added back get_size and clear_log tests, and xfail
@pytest.mark.xfail
def test_MD_insert_message_failure():
    logDB = MD.MicroserviceDB('TestDB.sqlite')
    with pytest.raises(TypeError):
        logDB.insert_into_Logs(TIME.get_timestamp(),'TRANSACTION',18)
<<<<<<< HEAD
=======
>>>>>>> Rewrote test_LogDatabase to fit SQLlite queries
=======
>>>>>>> Added back get_size and clear_log tests, and xfail
