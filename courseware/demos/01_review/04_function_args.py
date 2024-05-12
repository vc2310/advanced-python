from typing import Any

# the asterisk is called the "packing" operator
# def do_it(a: int, b: int, *c: int) -> None:
#     print(a, b, c)


# do_it(1, 2, 3, 4, 5, 6)


# the double asterisk is called the "dictionary packing" operator
# def do_it(a: int, b: int, **c: int) -> None:
#     print(a, b, c)


# do_it(1, b=2, g=2, d=4, y=3)

# when the "*" or "**" are used on the left-hand side of assignment
# they act as the packing operator capturing values into a data structure


def do_it(*args: Any, **kwargs: Any) -> None:
    print(args, kwargs)


the_args = [1, "test", True]
the_kwargs = {"k": 2, "l": "fun", "g": False}

# do_it(1, "test", True, k=2, l="fun", g=False)

# the "*" and "**" are the unpacking operation
# when the "*" or "**" are used on the right-hand side of assignment
# they act as the unpacking operator expanding values within an expression
do_it(*the_args, **the_kwargs)


print("Hello" + "!")
