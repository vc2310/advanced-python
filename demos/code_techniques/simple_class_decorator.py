from typing import Type, Any


def add_hello(cls: Type) -> Type:
    # Define a new method to add 'hello' to the class
    def say_hello(self: Any) -> str:
        return f"Hello, {self.name}!"

    # Add the new method to the class
    cls.say_hello = say_hello
    return cls





# Apply the class decorator to a class
@add_hello
class Person:
    def __init__(self, name: str):
        self.name = name

    def say_hello(self) -> str:
        return f"Hello, {self.name}!"


# Create an instance of the modified class
person = Person("Alice")

# # Call the added method
greeting = person.say_hello()  # type: ignore
print(greeting)  # Output: "Hello, Alice!"
