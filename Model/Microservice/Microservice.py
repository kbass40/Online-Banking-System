import json
import os
import sys
from pathlib import Path

import requests
from flask import Flask
from json2html import *

# Both parent directories need to be added to function from top-level as well as from local 
path = Path(__file__).parent.absolute()
sys.path.append(str(path) + '//..')
sys.path.append(str(path) + '//..//..')

from Model.Database import AuthenticationDatabase as ADB
from Model.Misc import Time as TIME

ACCESS_TOKEN = 'Wv62lOHnUq2EYwmmI9DMnfrrznrV'

SYMBOLS = {
	'oracle' : 'ORCL', 
	'google' : 'GOOGL', 
	'apple' : 'AAPL', 
	'facebook' : 'FB', 
	'ubisoft' : 'UBSFY'
	}

app = Flask(__name__)

class DB():
	def __init__(self):
		pass

auth = ADB.AuthDatabase()
db = DB()

@app.route("/api/<stock>/get-last", methods=["GET"])
def get_price(stock):
	if stock not in SYMBOLS:
		return "stock not found"

	response = requests.get('https://sandbox.tradier.com/v1/markets/quotes',
		params={'symbols': (SYMBOLS[stock] + ',VXX190517P00016000'), 'greeks': 'false'},
		headers={'Authorization': ('Bearer ' + ACCESS_TOKEN), 'Accept': 'application/json'}
	)
	json_response = response.json()
	ret = {
        'symbol' : json_response['quotes']['quote']['symbol'],
        'description' : json_response['quotes']['quote']['description'],
        'last' : json_response['quotes']['quote']['last']
    }
	
	auth.push_log(TIME.get_timestamp(), "INFO", stock + " price pull")

	return ret

@app.route('/api/<stock>/buy-stocks=<quantity>/<accountname>/<token>', methods=["GET"])
def user_buys_stocks(stock, quantity, accountname, token=None):
	validateToken(token)
	if stock not in SYMBOLS:
		return "stock not found"
	if not isinstance(quantity,str):
		raise TypeError('ERROR: quantity must be of type string')
	if not quantity.isdigit():
		raise TypeError('ERROR: Quantity must be of type int')
	if not auth.is_valid_account_for_user(token, accountname):
		return "account not found"

	price_per_stock = get_price(stock)['last']

	bank_info = auth.get_bank_info(SYMBOLS[stock])
	bank_quantity = bank_info['gain-loss']
	bank_gainloss = bank_info['stock_num']

	if get_account_balance(accountname, token) < (price_per_stock * int(quantity)):
		return "not enough funds"

	# check if the bank has enough stocks
	if bank_quantity < int(quantity):
		bank_gainloss = bank_gainloss - (price_per_stock * 5000)
		bank_quantity = bank_quantity + 5000
	else:
		bank_gainloss = bank_gainloss + (price_per_stock * int(quantity))
		bank_quantity = bank_quantity - int(quantity)

	# update bank information in firebase
	auth.update_bank_info(SYMBOLS[stock], bank_quantity, bank_gainloss)

	account_info = auth.get_account_info(token, accountname)
	user_gainloss = account_info[SYMBOLS[stock]]['gain-loss'] - (price_per_stock * int(quantity))
	user_quantity = account_info[SYMBOLS[stock]]['stock_num'] + int(quantity)
	# add stocks to the user account
	auth.update_user_info(token, accountname, SYMBOLS[stock], user_quantity, user_gainloss)

	auth.push_log(TIME.get_timestamp(), "TRANSACTION", "user buys " + str(quantity) + " " + stock + " stocks")

	# returns dictionary with 'gain-loss' and 'stock_num'
	return auth.get_account_info(token, accountname)[SYMBOLS[stock]]

@app.route('/api/<stock>/sell-stocks=<quantity>/<accountname>/<token>', methods=["GET"])
def user_sells_stocks(stock, quantity, accountname, token=None):
	if stock not in SYMBOLS:
		return "stock not found"
	validateToken(token)
	if not isinstance(quantity,str):
		raise TypeError('ERROR: quantity must be of type string')
	if not quantity.isdigit():
		raise TypeError('ERROR: Quantity must be of type int')
	if not auth.is_valid_account_for_user(token, accountname):
		return "account not found"

	price_per_stock = get_price(stock)['last']

	bank_info = auth.get_bank_info(SYMBOLS[stock])
	bank_gainloss = bank_info['gain-loss'] - (int(quantity) * price_per_stock)
	bank_quantity = bank_info['stock_num'] + (int(quantity))

	account_info = auth.get_account_info(token, accountname)

	if account_info[SYMBOLS[stock]]['stock_num'] < int(quantity):
		return "not enough stocks to sell"

	# update bank information in firebase
	auth.update_bank_info(SYMBOLS[stock], stock_amt=bank_quantity, gainloss=bank_gainloss)

	user_gainloss = account_info[SYMBOLS[stock]]['gain-loss'] + (int(quantity) * price_per_stock)
	user_quantity = account_info[SYMBOLS[stock]]['stock_num'] - int(quantity)
	# add stocks to the user account
	auth.update_user_info(token, accountname, SYMBOLS[stock], user_quantity, user_gainloss)

	auth.push_log(TIME.get_timestamp(), "TRANSACTION", "user sells " + str(quantity) + " " + stock + " stocks")

	# returns dictionary with 'gain-loss' and 'stock_num'
	return auth.get_account_info(token, accountname)[SYMBOLS[stock]]

@app.route('/api/add_to_balance=<value>/<accountname>/<toke>', methods=["GET"])
def user_adds_money(value, accountname, token=None):
	validateToken(token)
	if not isinstance(value,str):
		raise TypeError('ERROR: value must be of type string')
	if not value.isdigit():
		raise TypeError('ERROR: value must be of type int')
	if not auth.is_valid_account_for_user(token, accountname):
		return "account not found"

	auth.update_user_balance(token, accountname, value)

	auth.push_log(TIME.get_timestamp(), "TRANSACTION", "user added " + str(value) + " to account " + accountname)

	# TODO what to return here
	return "user adds to balance"

@app.route('/api/get-accounts/<token>', methods=["GET"])
def get_user_accounts(token=None):
	validateToken(token)

	accounts = auth.get_user_accounts(token)
	if accounts is None:
		return {}
	else:
		return accounts

@app.route('/api/get-account-balance/<accountname>/<token>', methods=["GET"])
def get_account_balance(accountname, token=None):
	validateToken(token)

	if not auth.is_valid_account_for_user(token, accountname):
		return "account not found"

	return auth.get_account_balance(accountname, token)

def validateToken(token):
	if token is not None:
		try:
			user = auth._get_userID_from_authID(token)
			if user is None:
				return "User not signed in"
		except:
			return "Invalid token"
	else:
		return "No token"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)