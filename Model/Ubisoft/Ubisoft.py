from flask import Flask
import requests
import json

UBISOFT_TOKEN = '6GrgiMPAz7nu1wWPOvG69AEVLFAd'
UBISOFT_SYMBOL = 'UBSFY'
STOCK_URL = 'https://sandbox.tradier.com/v1/markets/quotes'

app = Flask(__name__)

@app.route("/api/ubisoft/get-last", methods=["GET"])
def get_price():

    response = requests.get(STOCK_URL,
        params={'symbols': (UBISOFT_SYMBOL), 'greeks': 'false'},
        headers={'Authorization': ('Bearer ' + UBISOFT_TOKEN), 'Accept': 'application/json'}
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