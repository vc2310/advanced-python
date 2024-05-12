nums = [1, 2, 3, 4, 5]

# unpacking
# first, second, third = nums

# print(first)
# print(second)
# print(third)

# unpacking the elements from `nums`, keeping one element unpacked and assigned
# to first, and re-packing the remaining elements into `others`
# first, *others, last = "python"
# #      ^ packing

# print(first)
# print(others)
# print(last)

nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8]

# is the asterisk the packing or unpacking operator?
nums = [*nums1, *nums2]
print(nums)

# packing operator
# *<variable> = <iterable>

# unpacking operator
# <variable> = [*<iterable>]
