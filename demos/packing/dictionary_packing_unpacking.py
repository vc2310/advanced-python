# person = {"first_name": "Bob", "last_name": "Smith"}

# person2 = {"age": 42, **person}

# print(person2)


# def do_it(a: str, b: str, c: str) -> None:
#     print(a, b, c)

def do_it(**r) -> None:
    print(r)


do_it(a=2, b=4)
