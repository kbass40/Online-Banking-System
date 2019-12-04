from Model.Microservice import Microservice as MICROSERVICE
import pytest

# developer test
def test_fail_get_stock_price():
	stock = MICROSERVICE.get_price("invalidstock")
	assert stock == "Stock not found"

# developer test
def test_fail_validate_token():
	token = MICROSERVICE.validateToken("badToken")
	assert token == "Invalid token" or token == "User not signed in"

# developer test
def test_fail_buy_stocks_from_non_int_quantity_type():
    with pytest.raises(TypeError):
        MICROSERVICE.user_buys_stocks("oracle", "12.5", "invalidaccount", "invalidtoken")

# developer test
def test_fail_buy_stocks_from_raw_int_quantity_type():
    with pytest.raises(TypeError):
        MICROSERVICE.user_buys_stocks("oracle", 12.5, "invalidaccount", "invalidtoken")

# developer test
def test_fail_buy_stocks_from_with_bad_stock():
	stock = MICROSERVICE.user_buys_stocks("badstock", "12", "invalidaccount", "invalidtoken")
	assert stock == "Stock not found"

# developer test
def test_fail_sell_stocks_from_non_int_quantity_type():
    with pytest.raises(TypeError):
        MICROSERVICE.user_sells_stocks("oracle", "12.5", "invalidaccount", "invalidtoken")

# developer test
def test_fail_sell_stocks_from_raw_int_quantity_type():
    with pytest.raises(TypeError):
        MICROSERVICE.user_sells_stocks("oracle", 12.5, "invalidaccount", "invalidtoken")

# developer test
def test_fail_sell_stocks_from_with_bad_stock():
	stock = MICROSERVICE.user_sells_stocks("badstock", 12, "invalidaccount", "invalidtoken")
	assert stock == "Stock not found"

# developer test
def test_fail_add_money_with_bad_value_type():
	with pytest.raises(TypeError):
		MICROSERVICE.user_adds_money(12.5, "accountname")

# developer test
def test_fail_add_money_with_int_type():
	value = MICROSERVICE.user_adds_money("value", "accountname")
	assert value == "ERROR: value must be of type float"