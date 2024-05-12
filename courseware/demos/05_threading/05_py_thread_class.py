""" py thread class """

import threading


class SomeThread(threading.Thread):
    """some thread"""

    def __init__(self, msg: str):
        threading.Thread.__init__(self)
        self.msg = msg

    # required
    def run(self) -> None:
        print(self.msg + " thread starting " + str(threading.get_native_id()))
        self.whoami("run method")

    def whoami(self, location: str) -> None:
        """whoami"""
        print(f"{self.msg}, {location}, {threading.get_native_id()}")


some_thread = SomeThread("some thread object")
some_thread.start()  # the start methods calls the run method of the class

# will this code run on the new thread or the main thread?
some_thread.whoami("main script")

some_thread.join()
