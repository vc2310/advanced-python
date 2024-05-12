""" task async """

import asyncio
from random import randint
import time


def delay() -> float:
    """delay"""
    return randint(1, 10) / 2


async def get_data(task_num: int) -> int:
    """get data"""
    print("start get data")
    # time.sleep(delay())
    await asyncio.sleep(delay())
    print("end get data")
    return task_num


async def main() -> None:
    """main"""

    def all_done(t: asyncio.Task) -> None:
        print(f"all done : task {t.result()}")

    coroutine_obj = get_data(1)
    print(f"create corouting object: {type(coroutine_obj)}")

    task1 = asyncio.create_task(coroutine_obj)
    print("task 1 created")
    await asyncio.sleep(0.1)
    task1.add_done_callback(all_done)

    while not task1.done():
        print("task not done")
        await asyncio.sleep(0.1)
    # # await task1


if __name__ == "__main__":
    asyncio.run(main())
