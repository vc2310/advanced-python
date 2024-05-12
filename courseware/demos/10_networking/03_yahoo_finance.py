"""yahoo finance"""

import re
import requests

stock_price_re = re.compile(
    r"data-symbol=\"MSFT\".*?data-field=\"regularMarketPrice\".*?><span>(.*?)<"
)

headers = {"User-agent": "Mozilla/5.0"}

resp = requests.get(
    "https://finance.yahoo.com/quote/MSFT", timeout=60, headers=headers
)

# print(resp.text)

result = stock_price_re.findall(resp.text)
msft_price = float(result[0])

print(f"MSFT: ${msft_price} per share")
