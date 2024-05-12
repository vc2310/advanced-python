# type: ignore


class CustomContextManager:
    def __enter__(self):
        # Code to run before entering the context
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        # Code to run after exiting the context
        print("Exiting the context")

        if exc_type is not None:
            # Handle exceptions if they occurred within the context
            print(
                (
                    f"An exception of type {exc_type} "
                    f"occurred with value: {exc_value}"
                )
            )
            # return False  # Propagate the exception
            return True  # Do not propagate the exception


def main() -> None:
    # Usage of the custom context manager
    try:
        with CustomContextManager():
            print("Inside the context")
            # Simulate an error by dividing by zero
            result = 1 / 0
            print(result)
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")

    # After the context, it will automatically exit


if __name__ == "__main__":
    main()
