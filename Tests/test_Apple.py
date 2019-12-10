from Model.Microservice import Microservice as APPLE
import pytest

STOCK = APPLE

def test_fail_buy_stocks_from_invalid_quantity_type():
    with pytest.raises(TypeError):
        APPLE.user_buys_stocks(STOCK, None, None)

def test_fail_buy_stocks_from_non_int_quantity_type():
    with pytest.raises(TypeError):
        APPLE.user_buys_stocks(STOCK, "24.444", "testAccountName")

def test_fail_buy_stocks_from_raw_int_quantity_type():
    with pytest.raises(TypeError):
        APPLE.user_buys_stocks(STOCK, 52, "testAccountName")

def test_fail_sell_stocks_from_invalid_quantity_type():
    with pytest.raises(TypeError):
        APPLE.user_sells_stocks(STOCK, None, None)

def test_fail_sell_stocks_from_non_int_quantity_type():
    with pytest.raises(TypeError):
        APPLE.user_sells_stocks(STOCK, "25.9999", "testAccountName")

def test_fail_sell_stocks_from_raw_int_quantity_type():
    with pytest.raises(TypeError):
        APPLE.user_buys_stocks(STOCK, 25, "testAccountName")
