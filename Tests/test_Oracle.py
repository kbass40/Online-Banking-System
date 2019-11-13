from Model.Oracle import Oracle as ORACLE
import pytest

def test_fail_buy_stocks_from_invalid_quantity_type():
    with pytest.raises(TypeError):
        ORACLE.user_buys_stocks("not numbers")

def test_fail_buy_stocks_from_non_int_quantity_type():
    with pytest.raises(TypeError):
        ORACLE.user_buys_stocks("12.5")

def test_fail_buy_stocks_from_raw_int_quantity_type():
    with pytest.raises(TypeError):
        ORACLE.user_buys_stocks(12.5)

def test_fail_sell_stocks_from_invalid_quantity_type():
    with pytest.raises(TypeError):
        ORACLE.user_sells_stocks("not numbers")

def test_fail_sell_stocks_from_non_int_quantity_type():
    with pytest.raises(TypeError):
        ORACLE.user_sells_stocks("12.4")

def test_fail_sell_stocks_from_raw_int_quantity_type():
    with pytest.raises(TypeError):
        ORACLE.user_sells_stocks(12.5)

def test_jsonify():
	dict = [("-282050.0","5000"), ("-451280.0", "8000")]
	json = ORACLE.jsonify(dict)
	assert json == {1:{"gainloss":"-282050.0","quantity":"5000"},2:{"gainloss":"-451280.0","quantity":"8000"}}