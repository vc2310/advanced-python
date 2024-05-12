"""process data"""

import threading
import multiprocessing as mp
from multiprocessing.sharedctypes import Synchronized
from typing import cast


def increment_counter(counter: Synchronized) -> None:
    """increment counter"""

    with counter.get_lock():
        counter.value = counter.value + 1
        print(counter.value)


def main() -> None:
    """main"""

    counter: Synchronized = cast(Synchronized, mp.Value("i", 0))
    process_list = []

    for _ in range(16):
        # the_process = threading.Thread(target=increment_counter)
        the_process = mp.Process(target=increment_counter, args=(counter,))
        the_process.start()
        process_list.append(the_process)

    for a_process in process_list:
        a_process.join()

    # print(f"final counter: {counter[0]}")
    print(f"final counter: {counter.value}")


if __name__ == "__main__":
    main()
