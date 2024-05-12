import urllib.request
import json


url = "http://127.0.0.1:5055/api/2021-04-08?base=INR&symbols=USD,EUR"

with urllib.request.urlopen(url) as response:
    response = json.loads(response.read())
    print(response)
