"""This module demonstrates the use of multiple dispatch in Python."""

# to run this code install multipledispatch
# > pip install multipledispatch

from multipledispatch import dispatch


@dispatch(int, int)
def add(a, b):
    print("add two numbers")
    return a + b


@dispatch(int, int, int)  # type: ignore
def add(a, b, c):
    print("add three numbers")
    return a + b + c


print(add(1, 2))
print(add(1, 2, 3))
