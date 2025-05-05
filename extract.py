import requests

def extract(url, params):
    response = requests.get(url, params = params)
    data = response.json()
    return data


