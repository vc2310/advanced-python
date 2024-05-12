""" params decorator """

from typing import Any, Callable


class App:
    """app"""

    def __init__(self) -> None:
        self.__routes: dict[str, Callable[..., Any]] = {}

    def route(
        self, path: str
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """route"""

        def wrapper(fn: Callable[..., Any]) -> Callable[..., Any]:
            """wrapper"""

            def inner(*args: tuple[Any], **kwargs: dict[str, Any]) -> Any:
                """inner"""
                print(f"path: {path}")
                return fn(*args, **kwargs)

            self.__routes[path] = inner

            return inner

        return wrapper

    def run(self, path: str, *args: Any, **kwargs: Any) -> Any:
        """run"""
        fn = self.__routes[path]
        return fn(*args, **kwargs)


app = App()


@app.route("/add")
def add(a: int, b: int) -> int:
    """add"""
    return a + b


@app.route("/subtract")
def subtract(a: int, b: int) -> int:
    """subtract"""
    return a - b


print(app.run("/add", 1, 2))
print(app.run("/subtract", 1, 2))
