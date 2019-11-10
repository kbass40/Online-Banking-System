from flask import Flask
from Misc import Time as TIME
import requests
import json
import OracleDB
from json2html import *

ACCESS_TOKEN = 'Wv62lOHnUq2EYwmmI9DMnfrrznrV'
SYMBOL = 'ORCL'

app = Flask(__name__)


class Logger():
    def __init__(self):
        self._db = OracleDB.DBConnection()

    def get_log_size(self):
        return self._db.get_size()

    def clear(self,commit=False):
        self._db.clear_Logs(commit)

    def log_transaction(self,message,typing='TRANSACTION',commit=True):
        if not isinstance(message,str):
            raise TypeError('ERROR: Message must be of type string')

        if typing not in OracleDB.types:
            raise ValueError('ERROR: typing must be a defined log type')

        self._db.insert_into_Logs(TIME.get_timestamp(),typing,message,commit)

    def get_logs(self):
        return self._db.get_logs()


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
    log = Logger()
    log.log_transaction(('Retrieved stock information: ' + str(ret)), 'INFO')
    return ret

@app.route("/api/oracle/get-logs", methods=["GET"])
def get_logs():
    log = Logger()
    table = log.get_logs()
    return json2html.convert(json=table)

if __name__ == "__main__" :
    app.run(host="0.0.0.0")