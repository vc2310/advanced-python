from collections import OrderedDict
from decimal import Decimal


def main() -> None:
    pass

    current_prices: OrderedDict[str, Decimal] = OrderedDict(
        {
            "MSFT": Decimal("260.12"),
            "AAPL": Decimal("152.34"),
            "FLO": Decimal("27.17"),
        }
    )

    # for key, value in current_prices.items():
    #     print(key, value)

    # current_prices.move_to_end("MSFT")
    # current_prices.move_to_end("FLO", last=False)

    # print("after moving")
    # for key, value in current_prices.items():
    #     print(key, value)

    first = current_prices.popitem(last=False)
    last = current_prices.popitem(last=True)

    print(first)
    print(last)
    print(current_prices)


if __name__ == "__main__":
    main()
