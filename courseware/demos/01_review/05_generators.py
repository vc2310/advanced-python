from typing import Generator


def my_range(limit: int) -> Generator[int, None, None]:
    x = 0
    while x < limit:
        print("in the while loop")
        yield x
        x += 1


for num in my_range(10):
    print("in the for loop")
    print(num)
