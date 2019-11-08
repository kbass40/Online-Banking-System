from flask import Flask
import requests
import json
import OracleDB

ACCESS_TOKEN = 'Wv62lOHnUq2EYwmmI9DMnfrrznrV'
SYMBOL = 'ORCL'

app = Flask(__name__)

@app.route("/oracle/get-last", methods=["GET"])
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
    return ret

if __name__ == "__main__" :
    app.run(host="0.0.0.0")