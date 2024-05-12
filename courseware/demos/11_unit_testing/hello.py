"""hello module"""

import os
import yaml


class EmptyStringError(BaseException): ...


def hello(subject: str) -> str:
    """hello function"""

    if not subject:
        raise EmptyStringError("subject cannot be empty")

    return "hello, " + subject


def print_path() -> None:
    """print the path environment variable"""
    print(os.getenv("PATH"))


class WebServerConfig:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    @property
    def server_name(self):
        return f"{self.host}:{self.port}"

    # override the == operator to determine the objects are the same if the data attributes are the same
    def __eq__(self, other):
        if isinstance(other, WebServerConfig):
            return self.host == other.host and self.port == other.port
        return False


def read_web_server_config(file_path: os.PathLike[str]):
    """read a yaml config file"""
    with open(file_path, "r", encoding="UTF-8") as config_file:
        config = yaml.safe_load(config_file)

        web_server_config = WebServerConfig(
            config["server"]["host"], config["server"]["port"]
        )

        return web_server_config
