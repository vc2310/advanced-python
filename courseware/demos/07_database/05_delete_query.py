""" params query """

from connection_info import (
    connect_to_database,
    command_database,
    docker_conn_options,
)


def run() -> None:
    """run"""

    with connect_to_database(docker_conn_options) as conn:
        command_database(
            conn,
            "delete from rates where ratesid = ?",
            [6],
        )


if __name__ == "__main__":
    run()
