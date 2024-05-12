""" process shared data """

import multiprocessing as mp

# from multiprocessing.sharedctypes import Synchronized

counter = 0
print(f"top counter id: {id(counter)}")


def increment_counter() -> None:
    """increment counter"""
    global counter

    counter += 1
    print(f"increment counter: {counter}")
    print(f"in func counter id: {id(counter)}")


def main() -> None:
    """main"""

    process_list = []

    print(f"initial counter: {counter}")

    for _ in range(16):
        the_process = mp.Process(target=increment_counter)
        the_process.start()
        process_list.append(the_process)

    for a_process in process_list:
        a_process.join()

    print(f"final counter: {counter}")


print(f"__name__: {__name__}")
if __name__ == "__main__":
    mp.set_start_method("spawn")
    main()
