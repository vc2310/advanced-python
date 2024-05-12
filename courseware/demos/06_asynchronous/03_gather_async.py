""" gather async """

import asyncio
from random import randint
import time


def delay() -> float:
    """delay"""
    return randint(1, 10) / 2


counter = 0


async def get_data(task_num: int) -> int:
    global counter

    """get data"""
    print(f"start get data: {task_num}")
    await asyncio.sleep(delay())
    print(f"end get data: {task_num}")
    x = counter
    time.sleep(1)
    x += 1
    counter = x

    return task_num


async def main() -> None:
    """main"""

    # gather is going to wait for all three async operations to complete
    coroutine_objs = [get_data(1), get_data(2), get_data(3)]
    results = await asyncio.gather(*coroutine_objs)
    print(f"done: {results}")
    print(f"counter: {counter}")


if __name__ == "__main__":
    asyncio.run(main())
