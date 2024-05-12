nums = [1, 2, 3, 4, 5]

# option 1 - is not a real option
# for (idx=0; idx<len(nums); idx += 1):
#     print(nums[idx])

# option 2
# this code is very imperative (what and how)
# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# option 3
# this is more declarative compared to the while loop
# in more declarative code (what), but the "how" is handled by the runtime
# for num in nums:
#     print(num)


# idx = 0
# while idx < 10:
#     print(idx)
#     idx += 1

# my_rng = range(10)
# print(my_rng)
# my_iter_rng = iter(my_rng)
# print(my_iter_rng)

# print(next(my_iter_rng))
# print(next(my_iter_rng))
# print(next(my_iter_rng))

# for idx in range(10):
#     print(idx)

# double_nums = []
# for num in nums:
#     double_nums.append(num * 2)

# print(double_nums)


# double_nums = list(map(lambda num: num * 2, nums))
# print(double_nums)


# double_nums = [num * 2 for num in nums]
# print(double_nums)

print(enumerate(nums))

for idx, num in enumerate(nums):
    print(idx, num)
