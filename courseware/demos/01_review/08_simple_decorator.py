from typing import Any, Callable

# Callable[ [<param1_type>,<param2_type>,...], <return type> ]

# To accept any parameters:
# Callable[ ..., <return type> ]


def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
    # this is only defining the function "inner", the "inner" function
    # is NOT being invoked here
    def inner(*args: Any, **kwargs: Any) -> Any:
        # code that is being wrapped around "fn" is here
        print("call code before calling the function 'fn'")
        result = fn(*args, **kwargs)
        print("call code after calling the function 'fn'")
        return result

    # returning a reference to the "inner" function, it is not being invoked
    return inner


# do_it_wrapped = wrapper(do_it)
@wrapper
def do_it(a: int, b: int) -> int:
    return a + b


print(do_it(1, 2))

# the "do_it" function is NOT being invoked
# passing a object reference to the "do_it" function
# as an argument to the "wrapper" function
# do_it_wrapped = wrapper(do_it)
# print(type(do_it_wrapped))

# # this is where the "inner" function is invoked
# print(do_it_wrapped(1, 2))
