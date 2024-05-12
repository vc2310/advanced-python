""" fetch one """

from connection_info import (
    connect_to_database,
    create_cursor,
    docker_conn_options,
)


def run() -> None:
    """run"""

    with connect_to_database(docker_conn_options) as conn:
        with create_cursor(conn) as cur:
            cur.execute("select * from rates where ratesid = 1")

            rate = cur.fetchone()

            if rate:
                print("record exists")
                print(rate)


if __name__ == "__main__":
    run()
