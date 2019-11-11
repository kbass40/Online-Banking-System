from flask import Flask
from Misc import Time as TIME
import requests
import json
import OracleDB
from json2html import *

ACCESS_TOKEN = 'Wv62lOHnUq2EYwmmI9DMnfrrznrV'
SYMBOL = 'ORCL'

app = Flask(__name__)

class DB():
    def __init__(self):
        self._db = OracleDB.DBConnection()

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

        if typing not in OracleDB.types:
            raise ValueError('ERROR: typing must be a defined log type')

        self._db.insert_into_Logs(TIME.get_timestamp(),typing,message,commit)

    def insert_into_stocks(self, gainloss, quantity):
        self._db.insert_into_stocks(gainloss, quantity)

    def get_logs(self):
        return self._db.get_logs()

    def get_stocks(self):
        return self._db.get_stocks()


db = DB()

@app.route("/api/oracle/get-last", methods=["GET"])
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
    db.log_transaction(('Retrieved stock information: ' + str(ret)), 'INFO')
    return ret

@app.route("/api/admin/oracle/get-logs", methods=["GET"])
def get_logs():
    table = db.get_logs()
    # can change this to return json
    # using to view the logs while developing
    return json2html.convert(json=table)

# client wants to buy stocks
# if we have enough stocks sell them to client and increase gainloss
# if we dont have enough buy enough to sell to client and buy 5000 extra to hold on to for later
@app.route('/api/oracle/buy-stocks=<quantity>', methods=["GET"])
def user_buys_stocks(quantity):
    table = db.get_stocks()
    gainloss = table[-1][0]
    bank_quantity = table[-1][1]
    price = get_price()['last'] 
    if bank_quantity < int(quantity):
        gainloss = gainloss - (price * 5000)
        bank_quantity = bank_quantity + 5000
    else:
        gainloss = gainloss + (price * int(quantity))
        bank_quantity = bank_quantity - int(quantity)
    print(gainloss)
    print(bank_quantity)
    db.insert_into_stocks(gainloss, int(bank_quantity))
    table = db.get_stocks()
    return json2html.convert(json=table)


if __name__ == "__main__" :
    # delete later
    # using for testing purposes
    # clears bank balance so we start fresh each time running the app
    db.clear_stocks()
    size = db.get_stocks_size()
    if size == 0:
        print("Buy 5000 shares of oracle stock")
        val = get_price()['last'] * -5000
        db.insert_into_stocks(val, 5000)
    app.run(host="0.0.0.0")