import inspect


class DoIt:
    def run(self) -> None:
        print("Running...")


do_it = DoIt()

print(inspect.isclass(DoIt))  # True

print(inspect.isclass(do_it))  # False

print(inspect.isfunction(do_it.run))  # True

print(inspect.ismethod(do_it.run))  # True

print(inspect.getsource(do_it.run))  # print("Running...")
