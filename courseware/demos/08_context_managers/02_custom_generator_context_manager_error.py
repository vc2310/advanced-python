# type: ignore

from contextlib import contextmanager


@contextmanager
def custom_context_manager():
    # Code to run before entering the context
    print("Entering the context")

    try:
        # Yield control back to the caller
        yield
    except Exception as e:
        # Handle exceptions if they occurred within the context
        print(f"An exception occurred: {e}")
    finally:
        # Code to run after exiting the context
        print("Exiting the context")


def main() -> None:
    # Usage of the custom context manager
    try:
        with custom_context_manager():
            print("Inside the context")
            # Simulate an error by dividing by zero
            result = 1 / 0
            print(result)
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")

    # After the context, it will automatically exit


if __name__ == "__main__":
    main()
