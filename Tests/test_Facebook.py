from Model.Facebook import Facebook as FACEBOOK
import pytest

def test_fail_buy_stocks_from_invalid_quantity_type():
    with pytest.raises(TypeError):
        FACEBOOK.user_buys_stocks("none")

def test_fail_buy_stocks_from_non_int_quantity_type():
    with pytest.raises(TypeError):
        FACEBOOK.user_buys_stocks("34.15928")

def test_fail_buy_stocks_from_raw_int_quantity_type():
    with pytest.raises(TypeError):
        FACEBOOK.user_buys_stocks(60)

def test_fail_sell_stocks_from_invalid_quantity_type():
    with pytest.raises(TypeError):
        FACEBOOK.user_sells_stocks("none")

def test_fail_sell_stocks_from_non_int_quantity_type():
    with pytest.raises(TypeError):
        FACEBOOK.user_sells_stocks("3.14159")

def test_fail_sell_stocks_from_raw_int_quantity_type():
    with pytest.raises(TypeError):
        FACEBOOK.user_buys_stocks(30)
        
def test_jsonify():
	dict = [("-282050.0","5000"), ("-451280.0", "8000")]
	json = FACEBOOK.jsonify(dict)
	assert json == {1:{"gainloss":"-282050.0","quantity":"5000"},2:{"gainloss":"-451280.0","quantity":"8000"}}