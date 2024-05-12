from typing import Generator


def number_generator() -> Generator[int, int, None]:
    total = 0

    # generate an infinite sequence
    while True:
        # Yield the current total and receive a value from the caller
        x = yield total
        if x is None:
            continue  # Ignore None values
        total += x


# Example usage:
gen = number_generator()
next(gen)  # Initialize the generator

for i in range(1, 6):
    total = gen.send(
        i
    )  # Send a value to the generator and receive the updated total
    print(f"Total after adding {i}: {total}")

# Total after adding 1: 1
# Total after adding 2: 3
# Total after adding 3: 6
# Total after adding 4: 10
# Total after adding 5: 15
