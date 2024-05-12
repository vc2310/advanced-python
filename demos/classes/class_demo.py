from __future__ import annotations


class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def create(cls, full_name: str) -> Person:
        return cls(*cls.split_full_name(full_name))
        # first_name, last_name = cls.split_full_name(full_name)
        # return cls(first_name, last_name)

    # both lists and tuples are sequences
    # tuples - tuple is a sequence of related things that are different in type: (apple, 1.34, 3, a wholesome fruit)
    # lists - a list is a sequence of the same kind of thing in type: [apple, orange, steak, milk]

    @staticmethod
    def split_full_name(full_name: str) -> tuple[str, str]:
        fn, ln = full_name.split(" ")
        return fn, ln

    def __str__(self) -> str:
        return (
            f"<Person first_name={self.first_name}, "
            f"last_name={self.last_name}>"
        )


person = Person.create("Bob Smith")
print(person.full_name())
print(person)
