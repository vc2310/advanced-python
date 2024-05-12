from typing import Callable


# defining the function object
def add(a: int, b: int) -> int:
    return a + b


# defining the function object
def subtract(a: int, b: int) -> int:
    return a - b


def prepare_calc(
    math_fn: Callable[[int, int], int], x: int, y: int
) -> Callable[[], int]:
    # defining the do_calc function object
    def do_calc() -> int:
        # calling or invoking the math_fn function object
        return math_fn(x, y)

    # return a reference to do_calc
    return do_calc


# passing a reference to the function object
fn1 = prepare_calc(add, 4, 5)

# invoking the do_calc
print(fn1())

# print(do_calc(subtract, 6, 7))
