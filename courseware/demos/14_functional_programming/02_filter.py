def main() -> None:
    pass

    nums = range(20)
    even_nums = filter(lambda x: x % 2 == 0, nums)
    print(list(even_nums))


if __name__ == "__main__":
    main()
