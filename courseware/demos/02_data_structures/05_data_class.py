from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    city: str


def main() -> None:
    p = Person("John", 30, "New York")
    print(p)
    print(p.name)
    print(p.age)
    print(p.city)


if __name__ == "__main__":
    main()
