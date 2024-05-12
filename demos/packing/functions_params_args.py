from typing import Any


# *args - will collect the positional arguments
# **kwargs - will collect the keyword arguments
def do_it(*args: Any, **kwargs: Any) -> None:
    print(args)
    print(kwargs)


# 1, 2, 3, 4 are positional arguments
# a, b, c are keyword arguments
do_it(1, 2, 3, 4, "cool", a=2, b=3, d=5)
