""" params query """

from connection_info import (
    connect_to_database,
    query_database,
    docker_conn_options,
)


def run() -> None:
    """run"""

    currency_symbol = input("Please enter a currency symbol > ")

    with connect_to_database(docker_conn_options) as conn:
        with query_database(
            conn,
            "select * from rates where CurrencySymbol = ?",
            [currency_symbol],
        ) as rates:
            for rate_row in rates:
                print(rate_row)


if __name__ == "__main__":
    run()
