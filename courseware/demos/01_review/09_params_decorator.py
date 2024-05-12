from typing import Any, Callable


def skip_code(is_skipped: bool) -> Callable[..., Any]:
    def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
        def inner(*args: Any, **kwargs: Any) -> Any:
            if is_skipped:
                print("do not run the function")
            else:
                print("run the function")
                result = fn(*args, **kwargs)
                return result

        return inner

    return wrapper


@skip_code(False)
def do_it(a: int, b: int) -> int:
    return a + b


print(do_it(1, 2))
