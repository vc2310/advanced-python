from collections import deque


def main() -> None:
    d: deque[str] = deque(["a", "b", "c", "d", "e"])
    print(d)

    d.append("y")
    d.appendleft("z")
    print(d)

    # for i in d:
    #     print(i)

    # print(d.pop())
    # print(d.popleft())
    # print(d)

    d.rotate(3)
    print(d)

    # d.extend(["z", "z", "z"])
    # d.extendleft(["y", "y", "y"])

    # print(d)


if __name__ == "__main__":
    main()
