nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# imperative code
# do not write it this way
# counter = 0
# while counter < 10:
#     print(nums[counter])
#     counter += 1

# declarative code
# write it this way
# for num in nums:
#     print(num)

# double_nums = []

# for num in nums:
#     double_nums.append(num * 2)

# double_nums = [num * 2 for num in nums]


def multiply_by_2(x: int) -> int:
    print("inside multiply 2")
    return x * 2


double_nums = map(multiply_by_2, nums)

# iterate over it with list
# print(list(double_nums))

for double_num in double_nums:
    print("in for-in loop")
    print(double_num)
