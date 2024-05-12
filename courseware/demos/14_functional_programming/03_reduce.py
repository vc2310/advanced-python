from functools import reduce


def main() -> None:
    pass

    def double_it(accumulator: list[int], current_item: int) -> list[int]:
        # return value is the new accumulator
        print(f"acc: {accumulator}, cur: {current_item}")
        accumulator.append(current_item * 2)
        return accumulator

    double_nums: list[int] = reduce(double_it, range(20), [])
    print(double_nums)


if __name__ == "__main__":
    main()
