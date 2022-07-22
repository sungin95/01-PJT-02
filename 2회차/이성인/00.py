import requests

url = "https://api.bithumb.com/public/ticker/BTC_KRW"

response = requests.get(url)

data = response.json()

print(data.get('data').get('closing_price'))

