# type: ignore


class CustomContextManager:
    def __enter__(self):
        # Code to run before entering the context
        print("Entering the context")

    def __exit__(self, exc_type, exc_value, traceback):
        # Code to run after exiting the context
        print("Exiting the context")
        self.close()

    def close():
        ...


def main() -> None:
    # Usage of the custom context manager
    with CustomContextManager():
        print("Inside the context")

    # After the context, it will automatically exit


if __name__ == "__main__":
    main()
