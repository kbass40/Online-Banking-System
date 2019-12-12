import os
import sys
sys.path.append(os.path.abspath(".."))
from Database import AuthenticationDatabase as authdb
from flask import Flask
import Ubisoft as ubi

auth = authdb.AuthDatabase()

sym = "UBSFY"

app = Flask(__name__)

@app.route('/api/ubisoft/get-last/', methods=["Get"])
def get_price():
    return ubi.get_price(sym)

@app.route('/api/ubisoft/buy-stock=<quantity>/<token>', methods=["Get"])
def buy_stock(quantity, token):
    #check if token is valid
    if token is not None:
        try:
            u = auth.get_user_info(token)
        except Exception as e:
            #placeholder for now
            return str(e)
        
        return ubi.buy_stock(quantity, sym)
    else:
        #placeholder
        return 'Invalid Token'

@app.route('/api/ubisoft/sell-stock=<quantity>/<token>', methods=["Get"])
def sell_stock(quantity, token):
    #check if token is valid
    if token is not None:
        try:
            u = auth.get_user_info(token)
        except Exception as e:
            #placeholder for now
            return str(e)
        
        return ubi.sell_stock(quantity, sym)
    else:
        #placeholder
        return 'Invalid Token'

if __name__=="__main__":
    app.run(port=8000)