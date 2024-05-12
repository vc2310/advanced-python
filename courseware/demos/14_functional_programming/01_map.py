def main() -> None:
    pass

    def double(x: int) -> int:
        print(f"double called with {x}")
        return x * 2

    nums = range(20)
    # print(nums)
    # print(list(nums))

    # double_nums = []
    # for num in nums:
    #     double_nums.append(double(num))

    # print(double_nums)

    double_nums = map(double, nums)
    # print(next(double_nums))
    # print(next(double_nums))
    # print(next(double_nums))
    for double_num in double_nums:
        print(double_num)


if __name__ == "__main__":
    main()
