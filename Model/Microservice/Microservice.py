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
	# TODO log transaction in log database
	# db = DB()
    # db.log_transaction(('Retrieved stock information: ' + str(ret)), 'INFO')
	return ret

@app.route('/api/<stock>/buy-stocks=<quantity>/<token>', methods=["GET"])
def user_buys_stocks(stock, quantity, token=None):
	if stock not in SYMBOLS:
		return "stock not found"
	if token is not None:
		try:
			user = auth.get_user_info(token)
			if user is None:
				return "User not signed in"
		except:
			return "Invalid token"
	else:
		return "No token"
	if not isinstance(quantity,str):
		raise TypeError('ERROR: quantity must be of type string')
	if not quantity.isdigit():
		raise TypeError('ERROR: Quantity must be of type int')

	return "user buys stocks"

@app.route('/api/<stock>/sell-stocks=<quantity>/<token>', methods=["GET"])
def user_sells_stocks(stock, quantity, token=None):
	if stock not in SYMBOLS:
		return "stock not found"
	if token is not None:
		try:
			user = auth.get_user_info(token)
			if user is None:
				return "User not signed in"
		except:
			return "Invalid token"
	else:
		return "No token"
	if not isinstance(quantity,str):
		raise TypeError('ERROR: quantity must be of type string')
	if not quantity.isdigit():
		raise TypeError('ERROR: Quantity must be of type int')

	return "user sells stocks"

@app.route('/api/get-accounts/<token>', methods=["GET"])
def get_user_accounts(token=None):
	if token is not None:
		try:
			user= auth.get_user_info(token)
			if user is None:
				return "User not signed in"
		except:
			return "Invalid token"
	else:
		return "No token"

	# TODO get uid from token
	# uid = auth.get_uid_from_token(token)		

	return {
		1 : "account 1",
		2 : "account 2",
		3 : "account 3"
	}

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)