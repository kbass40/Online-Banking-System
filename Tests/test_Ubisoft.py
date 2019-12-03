from Model.Ubisoft import Ubisoft as UBISOFT
import pytest

def test_fail_buy_stocks_from_invalid_quantity_type():
    with pytest.raises(TypeError):
        UBISOFT.user_buys_stocks(None)

def test_fail_buy_stocks_from_non_int_quantity_type():
    with pytest.raises(TypeError):
        UBISOFT.user_buys_stocks("24.444")

def test_fail_buy_stocks_from_raw_int_quantity_type():
    with pytest.raises(TypeError):
        UBISOFT.user_buys_stocks(52)

def test_fail_sell_stocks_from_invalid_quantity_type():
    with pytest.raises(TypeError):
        UBISOFT.user_sells_stocks(None)

def test_fail_sell_stocks_from_non_int_quantity_type():
    with pytest.raises(TypeError):
        UBISOFT.user_sells_stocks("25.99999")

def test_fail_sell_stocks_from_raw_int_quantity_type():
    with pytest.raises(TypeError):
        UBISOFT.user_buys_stocks(25)
        
def test_jsonify():
	dict = [("-282050.0","5000"), ("-451280.0", "8000")]
	json = UBISOFT.jsonify(dict)
	assert json == {1:{"gainloss":"-282050.0","quantity":"5000"},2:{"gainloss":"-451280.0","quantity":"8000"}}