import asyncio


async def main() -> None:
    print("did it run?")


if __name__ == "__main__":
    # put the coroutine object into an event loop
    # the asyncio.run create an event loop, one
    # event loop may be created per thread
    asyncio.run(main())
