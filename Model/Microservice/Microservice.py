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

auth = ADB.AuthDatabase()

@app.route("/api/<stock>/get-last", methods=["GET"])
def get_price(stock):
	if stock not in SYMBOLS:
		return 404

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
		return 404
	if token is not None:
		try:
			user = auth.get_user_info(token)
			if user is None:
				return 404
		except:
			return 404
	if not isinstance(quantity, str):
		return 404
	if not quantity.isdigit():
		return 404

	return "user buys stocks"

@app.route('/api/<stock>/sell-stocks=<quantity>/<token>', methods=["GET"])
def user_sells_stocks(stock, quantity, token=None):
	if stock not in SYMBOLS:
		return 404
	if token is not None:
		try:
			user = auth.get_user_info(token)
			if user is None:
				return 404
		except:
			return 404
	if not isinstance(quantity, str):
		return 404
	if not quantity.isdigit():
		return 404

	return "user sells stocks"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)