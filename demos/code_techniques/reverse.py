"""sorting"""

from random import randint


nums = [randint(0, 10) for _ in range(10)]

reverse_sorted_nums = reversed(sorted(nums))

print(reverse_sorted_nums)

print(list(reverse_sorted_nums))
