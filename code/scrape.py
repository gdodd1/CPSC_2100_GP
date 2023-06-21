import requests

def scrape():
    # Where USD is the base currency you want to use
    url = 'https://api.currencyapi.com/v3/latest?apikey=M93bPLOvQmQnMTJSF7RIUGUSYnpL8zncsjKJ1Nae'

    # Making our request
    response = requests.get(url)
    return response.json()
