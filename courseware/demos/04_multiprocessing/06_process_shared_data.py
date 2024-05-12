""" process shared data """

import multiprocessing as mp
from multiprocessing.sharedctypes import Synchronized


def increment_counter(counter: Synchronized) -> None:
    """increment counter"""

    # get a lock on the synchronized value before modifying
    # the lock ensures the modifications are safely done
    with counter.get_lock():
        counter.value += 1
        print(counter.value)
    # when execution exits the with block the lock is released


def main() -> None:
    """main"""

    # variable whose value is synchronized across process
    counter: Synchronized = mp.Value("i", 0)
    process_list = []

    for _ in range(16):
        # pass the synchronized variable into the args when
        # creating a new process
        the_process = mp.Process(target=increment_counter, args=(counter,))
        the_process.start()
        process_list.append(the_process)

    for a_process in process_list:
        a_process.join()

    print(f"final counter: {counter}")


if __name__ == "__main__":
    main()
