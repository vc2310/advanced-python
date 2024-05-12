# type: ignore

from contextlib import contextmanager


# Define a generator function for the context manager
@contextmanager
def custom_context_manager():
    # Code to run before entering the context
    print("Entering the context")

    # Yield control back to the caller
    yield

    # Code to run after exiting the context
    print("Exiting the context")


def main() -> None:
    # Usage of the custom context manager
    with custom_context_manager():
        print("Inside the context")

    # After the context, it will automatically exit


if __name__ == "__main__":
    main()
