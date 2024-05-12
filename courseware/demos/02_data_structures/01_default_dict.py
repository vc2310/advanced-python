from collections import defaultdict
from random import randint


def main() -> None:
    # person = {"first_name": "Bob", "last_name": "Smith", "age": 23}
    # print(person.get("age", 42))

    # start: defaultdict[str, int] = defaultdict(lambda: randint(0, 100))
    # start: defaultdict[str, int] = defaultdict(lambda: 0)

    # print(start["x"])
    # print(start["x"])

    # print(start["x"])
    # print(start["y"])
    # print(start["z"])
    # start["x"] = 10
    # print(start["x"])

    dict_of_lists: defaultdict[str, list] = defaultdict(list)
    print(dict_of_lists["x"])
    #
    dict_of_dicts: defaultdict[str, dict] = defaultdict(dict)
    print(dict_of_dicts["x"])
    #
    dict_of_ints: defaultdict[str, int] = defaultdict(int)
    print(dict_of_ints["x"])


if __name__ == "__main__":
    main()
