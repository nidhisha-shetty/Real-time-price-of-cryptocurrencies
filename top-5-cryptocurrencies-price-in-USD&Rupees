import requests
import json

def cur_con(url):
	response = requests.get(url)
	response_json = json.loads(response.text)
	b = response_json[0]["price_usd"]
	return(b)

list_url=["https://api.coinmarketcap.com/v1/ticker/bitcoin/",
		      "https://api.coinmarketcap.com/v1/ticker/ethereum/",
	        "https://api.coinmarketcap.com/v1/ticker/ripple/",
		      "https://api.coinmarketcap.com/v1/ticker/litecoin/",
		      "https://api.coinmarketcap.com/v1/ticker/factom/"]

for url in list_url:
  print("Price in USD: "+cur_con(url))
 	print("Price in rupees: "+str(float(cur_con(url))*70)+"\n")
