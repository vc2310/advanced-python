from typing import Type, Any, Callable


def add_greeting(greeting_message: str) -> Callable[[Type], Type]:
    def decorator(cls: Type) -> Type:
        # Define a new method using the parameter
        def greet(self: Any) -> str:
            return f"{greeting_message}, {self.name}!"

        # Add the new method to the class
        setattr(cls, "greet", greet)
        return cls

    return decorator


# Apply the class decorator with a parameter to a class
@add_greeting("Hi")
class Person:
    def __init__(self, name: str):
        self.name = name


# Create an instance of the modified class
person = Person("Alice")

# Call the added method
greeting = person.greet()  # type: ignore
print(greeting)  # Output: "Hi, Alice!"
