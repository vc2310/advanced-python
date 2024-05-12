import asyncio


async def get_data() -> None:
    # task 1
    print("start get data")

    # time.sleep but for asynchronous code
    await asyncio.sleep(3) # non-blocking on the thread

    # task 2
    print("end get data")


async def main() -> None:
    await get_data()


if __name__ == "__main__":
    # fire up the async runtime (event loop)
    # only have one event loop per thread
    asyncio.run(main())
