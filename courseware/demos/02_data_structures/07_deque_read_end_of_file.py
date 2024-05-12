from collections import deque
from pathlib import Path


def main() -> None:
    pass

    fruits_file_path = Path("data", "fruits.txt")
    with fruits_file_path.open(encoding="UTF-8") as fruits_file:
        fruits = deque(map(lambda x: x.strip(), fruits_file), 5)
        print(fruits)


if __name__ == "__main__":
    main()
