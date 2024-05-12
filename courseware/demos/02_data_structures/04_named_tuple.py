from collections import namedtuple


def main() -> None:
    Point = namedtuple("Point", ["x", "y"])

    # def calc_midpoint(start_point: Point, end_point: Point) -> Point:
    #     return Point(
    #         (start_point.x + end_point.x) / 2,
    #         (start_point.y + end_point.y) / 2,
    #     )

    # start = Point(1, 1)
    # end = Point._make([4, 7])

    # print(start)
    # print(start[0])
    # print(start.x)

    # mid = calc_midpoint(start, end)

    # x, y = mid

    # print(f"mid x: {x}, mid y: {y}")
    # print(f"mid x: {mid[0]}, mid y: {mid[1]}")
    # print(f"mid x: {getattr(mid, 'x')}, mid y: {getattr(mid, 'y')}")
    # print(f"mid x: {mid.x}, mid y: {mid.y}")

    p = Point(**{"x": 1, "y": 2})

    print(p)
    print(p._asdict())

    items: list[Point] = [Point(3, 4), Point(2, 3), Point(1, 2)]

    items.sort()
    print(items)


if __name__ == "__main__":
    main()
