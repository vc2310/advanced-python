message = "Hello, World!"


def do_it() -> None:
    message = "changed it"

    def do_it2() -> None:
        nonlocal message
        message = "changed it 2 "
        print("#1", message)

    do_it2()

    print("#2", message)


do_it()

print("#3", message)
