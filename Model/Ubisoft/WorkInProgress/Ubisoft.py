import os
import requests
import UbisoftDB

atoken = "J3z7DrPHATWESyoAN69cH6tZiybR"
endpoint = "https://sandbox.tradier.com/v1/markets/quotes"

#Gets the price of the stock specified by the symbol, returned as a json
def get_price(symbol):
    #headers for the request
    header = {
        "Accept": "application/json",
        "Authorization": "Bearer " + atoken
    }
    #parameters for the request
    param = {
        "symbols": str(symbol)
    }
    response = requests.get(endpoint, headers=header, params=param)
    json_response = response.json()

    output = {
        "symbol": json_response['quotes']['quote']['symbol'],
        "description": json_response["quotes"]["quote"]["description"],
        "last": json_response["quotes"]["quote"]["last"]
    }

    #still have to log it

    return output

def buy_stock(quantity, symbol):
    try:
        price = int(get_price(symbol)["last"]) * int(quantity)
    except:
        return "Input Error"

    #update users balance (make sure that the user is not trying to buy more than he is able to)
    #return updated user wallet (balance and stock amount)
    #make sure to log it

def sell_stock(quantity, symbol):
    try:
        price = int(get_price(symbol)["last"]) * int(quantity)
    except:
        return "Input Error"
    
    #update users balance (make sure that they are not trying to sell more stocks than they own)
    #return updated user wallet
    #make sure to log it


#if __name__=="__main__":
#    get_price("UBSFY")