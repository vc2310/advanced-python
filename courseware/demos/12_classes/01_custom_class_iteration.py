from __future__ import annotations


class CountingNumbers:
    limit: int
    current: int

    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.current = 0

    def __iter__(self) -> CountingNumbers:
        return self

    def __next__(self) -> int:
        if self.current < self.limit:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration


# Create an instance of CountingNumbers
numbers = CountingNumbers(5)

# numbers.__dict__["esri"] = "rocks!"

# for attr in numbers.__dict__:
#     print(attr)

# print(numbers.esri)

# Iterate through the custom iterable
for num in numbers:
    print(num)

# Output:
# 0
# 1
# 2
# 3
# 4
