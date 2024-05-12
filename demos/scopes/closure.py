from typing import Callable

# closure
# 1. requires two functions, one nested inside the other
# 2. a variable declared in the outer function but used in the inner function


def outer() -> tuple[Callable[[], None], Callable[[int], None]]:
    t = 2

    def modify_t(new_t: int) -> None:
        nonlocal t
        print("I was called")
        # creating a new local variable t within the modify_t function
        t += new_t

    def print_t() -> None:
        print(t)

    return print_t, modify_t


prt_t, mod_t = outer()

prt_t()  # 1st output 2
mod_t(4)
prt_t()  # 2nd output 4

prt_t2, mod_t2 = outer()

prt_t2()  # 1st output 2
mod_t2(7)
prt_t2()  # 2nd output 4

prt_t()  # 1st output 2
mod_t(4)
prt_t()  # 2nd output 4
