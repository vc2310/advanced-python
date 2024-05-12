# type: ignore

from functools import wraps


def wrapper(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        print("called from inner")
        return fn(*args, **kwargs)

    return inner  # not invoking the inner function, returning a ref to it


@wrapper
def do_it(a, b):
    """does something cool"""
    return a + b


# wrapped_do_it = wrapper(do_it)
# print(wrapped_do_it(1, 2))

print(do_it(1, 2))
