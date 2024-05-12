""" getting data from a website """

import requests
import re


national_currencies = ["usd", "cad", "eur", "hkd"]

crypt_name_re = re.compile("^Litecoin$|^Bitcoin$|^Ethereum$")


resp = requests.get("https://api.coingecko.com/api/v3/coins/list", timeout=60)

currencies = resp.json()

crypto_currencies = [
    currency
    for currency in currencies
    if crypt_name_re.match(currency["name"])
]

print(crypto_currencies)

for crypto_currency in crypto_currencies:

    resp = requests.get((
        "https://api.coingecko.com/api/v3/simple/price"
        f"?ids={crypto_currency['id']}&"
        f"vs_currencies={','.join(national_currencies)}"
    ), timeout=60)

    print(resp.json())
