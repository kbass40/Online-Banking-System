from flask import Flask
import requests
import json

APPLE_TOKEN = '6GrgiMPAz7nu1wWPOvG69AEVLFAd'
APPLE_SYMBOL = 'AAPL'
STOCK_URL = 'https://sandbox.tradier.com/v1/markets/quotes'

app = Flask(__name__)

@app.route("/api/apple/get-last", methods=["GET"])
def get_price():

    response = requests.get(STOCK_URL,
        params={'symbols': (APPLE_SYMBOL), 'greeks': 'false'},
        headers={'Authorization': ('Bearer ' + APPLE_TOKEN), 'Accept': 'application/json'}
    )

    info = {
        'symbol': response.json()['quotes']['quote']['symbol'],
        'description': response.json()['quotes']['quote']['description'],
        'last': response.json()['quotes']['quote']['last']
    }

    return info

def run_server():
    app.run(threaded=True, host='0.0.0.0', port='5000')

if __name__ == "__main__" :
    run_server()