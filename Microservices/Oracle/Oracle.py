import flask
import requests
import OracleDB

ACCESS_TOKEN = 'Wv62lOHnUq2EYwmmI9DMnfrrznrV'
SYMBOL = 'ORCL'

response = requests.get('https://sandbox.tradier.com/v1/markets/quotes',
    params={'symbols': (SYMBOL + ',VXX190517P00016000'), 'greeks': 'false'},
    headers={'Authorization': ('Bearer ' + ACCESS_TOKEN), 'Accept': 'application/json'}
)
json_response = response.json()
value = json_response['quotes']['quote']['last']
print(response.status_code)
print(value)