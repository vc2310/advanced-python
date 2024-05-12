""" execute many query """

import pyodbc

from connection_info import (
    connect_to_database,
    create_cursor,
    docker_conn_options,
)


def run() -> None:
    """run"""

    with connect_to_database(docker_conn_options) as conn:
        with create_cursor(conn) as cur:
            params = [
                ("2021-10-03", "INR", 80),
                ("2021-10-03", "USD", 1.10),
                ("2021-10-03", "GBP", 0.90),
                ("2021-10-03", "CAD", 1.40),
                ("2021-10-03", "BTC", 33000),
            ]

            cur.executemany(
                "insert into rates (closingdate, currencysymbol, exchangerate)"
                "values (?, ?, ?)",
                params,
            )


if __name__ == "__main__":
    run()
