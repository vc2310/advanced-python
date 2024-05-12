from typing import Any

# do_it("a", "b", "c")
# a, b, c = ("a", "b", "c")


# do_it(["a", "b", "c"])
# a, b, c = (["a", "b", "c"], None, None)


# do_it(*["a", "b", "c"])
# a, b, c = ("a", "b", "c")


# def do_it(a: Any = None, b: Any = None, c: Any = None) -> None:
#     print(a, b, c)

# do_it(*["a", "b", "c"])

# do_it(1, 2, 3, 4, 5, 6, 7)
# a, b, *c = (1, 2, 3, 4, 5, 6, 7)


# is the asterisk the packing or unpacking operator in this context?
def do_it(a: Any = None, b: Any = None, *c: Any) -> None:
    print(a, b, c)


do_it(1, 2, 3, 4, 5, 6, 7)
do_it(*[1, 2, 3, 4, 5, 6, 7])
