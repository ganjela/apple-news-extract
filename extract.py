import requests

def extract(url, params):
    response = requests.get(url, params = params)
    return response.json()


