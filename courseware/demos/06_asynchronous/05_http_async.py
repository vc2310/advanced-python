""" http async """
from typing import Any
import asyncio
import aiohttp
import requests
import time
import threading

urls = [
    ("http://127.0.0.1:5055/api/2021-04-08?base=INR&symbols=USD,EUR"),
] * 10


async def get_response(session: aiohttp.ClientSession, url: str) -> Any:
    """get coin price"""
    async with session.get(url) as resp:
        response = await resp.json()
        return response


async def main() -> None:
    """main"""

    start = time.time()

    # for url in urls:
    #     print(requests.get(url).json())

    # threads = []

    # for url in urls:
    #     threads.append(
    #         threading.Thread(
    #             target=lambda url: print(requests.get(url).json()), args=(url,)
    #         )
    #     )
    #     threads[-1].start()

    # for thread in threads:
    #     thread.join()

    async with aiohttp.ClientSession() as session:
        # execute as a group (provides benefit)
        prices = await asyncio.gather(
            *[get_response(session, url) for url in urls]
        )

        print(prices)

    # execute in sequence (provides no benefit when using async)
    # prices = []
    # for url in urls:
    #     prices.append(await get_coin_price(session, url))

    # print(prices)

    print(time.time() - start)


if __name__ == "__main__":
    asyncio.run(main())
