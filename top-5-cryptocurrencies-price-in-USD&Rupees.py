import requests
import json


def cur_con(url):
    response = requests.get(url)
    response_json = json.loads(response.text)
    return response_json[0]['current_price']
    

list_url=["https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin",
	"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ethereum",
	"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=ripple",
	"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=litecoin",
	"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=factom"]

for url in list_url:
    print("Price in USD: "+str(cur_con(url)))
    print("Price in Rupees: "+str(float(cur_con(url))*70)+"\n")
