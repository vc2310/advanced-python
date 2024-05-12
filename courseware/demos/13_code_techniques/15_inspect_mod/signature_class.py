from inspect import signature


def do_it(val, *, item_ids: list[int] = [], **kwargs): ...


sig = signature(do_it)

print(sig.parameters)

print(sig.parameters["val"].default)
print(sig.parameters["item_ids"].default)
print(sig.parameters["item_ids"].annotation)
