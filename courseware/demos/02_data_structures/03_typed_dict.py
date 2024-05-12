from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int
    city: str


def main() -> None:
    pass

    p: Person = {"name": "John", "age": 30, "city": "New York"}
    print(p)
    print(p["name"])
    print(p["age"])
    print(p["city"])


if __name__ == "__main__":
    main()
