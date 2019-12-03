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
from Model.Database import MicroserviceDB as AppleDB

ACCESS_TOKEN = "6GrgiMPAz7nu1wWPOvG69AEVLFAd"
SYMBOL = 'AAPL'

app = Flask(__name__)

class DB():
    def __init__(self):
        self._db = AppleDB.MicroserviceDB('AppleDB.sqlite')

    def get_log_size(self):
        return self._db.get_logs_size()

    def get_stocks_size(self):
        return self._db.get_stocks_size()

    def clear_logs(self,commit=False):
        self._db.clear_Logs(commit)

    def clear_stocks(self,commit=False):
        self._db.clear_Stocks(commit)

    def log_transaction(self,message,typing='TRANSACTION',commit=True):
        if not isinstance(message,str):
            raise TypeError('ERROR: Message must be of type string')

        if typing not in AppleDB.types:
            raise ValueError('ERROR: typing must be a defined log type')

        self._db.insert_into_Logs(TIME.get_timestamp(),typing,message,commit)

    def insert_into_stocks(self, gainloss, quantity):
        self._db.insert_into_stocks(gainloss, quantity)

    def get_logs(self):
        return self._db.get_logs()

    def get_stocks(self):
        return self._db.get_stocks()

auth = ADB.AuthDatabase()

@app.route("/api/apple/get-last", methods=["GET"])
def get_price():
    response = requests.get('https://sandbox.tradier.com/v1/markets/quotes',
        params={'symbols': (SYMBOL + ',VXX190517P00016000'), 'greeks': 'false'},
        headers={'Authorization': ('Bearer ' + ACCESS_TOKEN), 'Accept': 'application/json'}
    )
    json_response = response.json()
    ret = {
        'symbol' : json_response['quotes']['quote']['symbol'],
        'description' : json_response['quotes']['quote']['description'],
        'last' : json_response['quotes']['quote']['last']
    }
    db = DB()
    db.log_transaction(('Retrieved stock information: ' + str(ret)), 'INFO')
    return ret

@app.route("/api/admin/apple/get-logs", methods=["GET"])
def get_logs():
    db = DB()
    table = db.get_logs()
    return json2html.convert(json=table)

# client wants to buy stocks
# if we have enough stocks sell them to client and increase gainloss
# if we dont have enough buy enough to sell to client and buy 5000 extra to hold on to for later
@app.route('/api/apple/buy-stocks=<quantity>/<token>', methods=["GET"])
def user_buys_stocks(quantity, token=None):
    if token is not None:
        try:
            user = auth.get_user_info(token)
            if user is None:
                return "User not signed in"
        except:
            return "Inalid token"
    if not isinstance(quantity,str):
        raise TypeError('ERROR: quantity must be of type string')
    if not quantity.isdigit():
        raise TypeError('ERROR: Quantity must be of type int')
    db = DB()
    table = db.get_stocks()
    index = len(table)-1
    gainloss = table[index][0]
    bank_quantity = table[index][1]
    price = get_price()['last'] 
    if bank_quantity < int(quantity):
        gainloss = gainloss - (price * 5000)
        bank_quantity = bank_quantity + 5000
    else:
        gainloss = gainloss + (price * int(quantity))
        bank_quantity = bank_quantity - int(quantity)
    db.insert_into_stocks(gainloss, int(bank_quantity))
    table = db.get_stocks()
    table = jsonify(table)
    db.log_transaction(('Bank sells stocks to user: ' + str(table[len(table)])), 'TRANSACTION')
    return table[len(table)]

@app.route('/api/apple/sell-stocks=<quantity>/<token>', methods=["GET"])
def user_sells_stocks(quantity, token=None):
    if token is not None:
        try:
            user = auth.get_user_info(token)
            if user is None:
                return "User not signed in"
        except:
            return "Inalid token"
    if not isinstance(quantity,str):
        raise TypeError('ERROR: quantity must be of type string')
    if not quantity.isdigit():
        raise TypeError('ERROR: Quantity must be of type int')
    db = DB()
    table = db.get_stocks()
    index = len(table)-1
    gainloss = table[index][0]
    bank_quantity = table[index][1]
    price = get_price()['last'] 
    gainloss = gainloss - (price * int(quantity))
    bank_quantity = bank_quantity + int(quantity)
    db.insert_into_stocks(gainloss, int(bank_quantity))
    table = db.get_stocks()
    table = jsonify(table)
    db.log_transaction(('Bank buys stocks from user: ' + str(table[len(table)])), 'TRANSACTION')
    return table[len(table)]

def jsonify(table):
    json = {}
    for i, tup in enumerate(table):
        call = {
            "gainloss" : str(tup[0]),
            "quantity" : str(tup[1]),
        }
        json[i+1] = call
    return json


if __name__ == "__main__" :
    # delete first line later
    # using for testing purposes
    # clears bank balance so we start fresh each time running the app
    # db.clear_stocks()
    db = DB()
    size = db.get_stocks_size()
    authDB = ADB.AuthDatabase()
    print('Example authenticated token:\n\n'+authDB.authenticate_user_via_email_password('kyle@email.com','password')+'\n')
    if size == 0:
        print("Buy 5000 shares of apple stock")
        val = get_price()['last'] * -5000
        db.insert_into_stocks(val, 5000)
    app.run(host="0.0.0.0")
