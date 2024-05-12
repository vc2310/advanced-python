""" py thread """

# timeline     t=0                                                             t=n

# main thread:  1 -> 28           29 -> 31           32 -> 35      36    37 -> 38

# thread A:             15 -> 20                                21

# thread B:                                15 -> 20                   21

import time
import threading


def some_task() -> None:
    """some task"""

    print("task name: " + threading.current_thread().name)
    print("start some task: " + str(threading.get_native_id()))
    time.sleep(2)
    print("end some task: " + str(threading.get_native_id()))


print("main thread name: " + threading.current_thread().name)
print("main thread native id: " + str(threading.get_native_id()))

thread1 = threading.Thread(target=some_task, name="threadA")
thread1.start()

thread2 = threading.Thread(target=some_task, name="threadB")
thread2.start()

# blocking calls, in this case, we are waiting for the thread to finish
# before proceeding
thread1.join()
thread2.join()

print("end main thread: " + str(threading.get_native_id()))
