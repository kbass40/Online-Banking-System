from Model.Logger import Logger as LOGGER 
import pytest

#This test is supposed to fail
@pytest.mark.xfail
def test_log_transaction_message_failure():
    with pytest.raises(TypeError):
        myLogger = LOGGER.Logger()
        myLogger.log_transaction(23729)

#This test is supposed to fail
@pytest.mark.xfail
def test_log_transaction_typing_failure():
    with pytest.raises(ValueError):
        myLogger = LOGGER.Logger()
        myLogger.log_transaction("This test should fail because of a bad type",'FAKE_TYPE')

def test_log_transaction():
    myLogger = LOGGER.Logger()
    myLogger.clear()
    prev = myLogger.get_log_size()
    myLogger.log_transaction("The is from Logger's test",commit=False)
    assert prev+1 == myLogger.get_log_size()

def test_print_Logger():
    LOGGER.printLog()
