import multiprocessing as mp


def app_server(message: str) -> None:
    print(message)
    counter = 0
    while counter < 100000000:
        counter += 1


print(f"process name: {__name__}")

if __name__ == "__main__":
    print("ran create process")

    process1 = mp.Process(target=app_server, args=("hello, world",))

    # start the child (process1) process
    process1.start()
    print("process1 started")

    counter = 0
    while True:
        counter += 1
        print("process 1 is still alive")
        if not process1.is_alive():
            print("process 1 is no longer with us")
            break
        elif counter > 100:
            ...
            # process1.terminate()
            # process1.kill()

    # block the main process from executing until
    # the child (process1) process completes
    process1.join()
    print("process1 done")
