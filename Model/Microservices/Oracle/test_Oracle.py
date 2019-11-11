import pytest
from Oracle import *

def test_buy_stocks_accepts_int1():
    with pytest.raises(TypeError):
        user_buys_stocks("not numbers")

def test_buy_stocks_accepts_int2():
    with pytest.raises(TypeError):
        user_buys_stocks("12.5")

def test_buy_stocks_accepts_int3():
    with pytest.raises(TypeError):
        user_buys_stocks(12.5)

def test_sell_stocks_accepts_int1():
    with pytest.raises(TypeError):
        user_sells_stocks("not nnumbers")

def test_sells_stocks_accepts_int2():
    with pytest.raises(TypeError):
        user_sells_stocks("12.4")

def test_sells_stocks_accepts_int3():
    with pytest.raises(TypeError):
        user_sells_stocks(12.5)

def test_jsonify():
	dict = [("-282050.0","5000"), ("-451280.0", "8000")]
	json = jsonify(dict)
	assert json == {1:{"gainloss":"-282050.0","quantity":"5000"},2:{"gainloss":"-451280.0","quantity":"8000"}}