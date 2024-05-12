import asyncio

import requests
import aiohttp


urls = [
    ("http://127.0.0.1:5055/api/2021-04-08?base=INR&symbols=USD,EUR"),
] * 10


async def get_coin_price_async(
    session: aiohttp.ClientSession, url: str
) -> str:
    """get coin price"""
    async with session.get(url) as resp:
        return await resp.text()


def get_coin_price_sync(url: str) -> str:
    """get coin price"""
    return requests.get(url).text


async def main() -> None:
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(
            *[get_coin_price_async(session, url) for url in urls],
            *[asyncio.to_thread(get_coin_price_sync, url) for url in urls],
        )

    print(responses)


if __name__ == "__main__":
    asyncio.run(main())
