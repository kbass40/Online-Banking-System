from Model.Logger import Logger as LOGGER 
import pytest

def test_log_transaction_failure():
    with pytest.raises(TypeError):
        myLogger = LOGGER.Logger()
        myLogger.log_transaction(23729)

def test_log_transaction():
    myLogger = LOGGER.Logger()
    myLogger.clear()
    prev = myLogger.get_log_size()
    myLogger.log_transaction("The is from Logger's test",commit=False)
    assert prev+1 == myLogger.get_log_size()

def test_print_Logger():
    LOGGER.printLog()
