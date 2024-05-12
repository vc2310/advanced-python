""" params query """

from connection_info import (
    connect_to_database,
    command_database,
    docker_conn_options,
)


def run() -> None:
    """run"""

    closing_date = "2021-10-03"
    currency_symbol = "HKD"
    exchange_rate = 2.34

    with connect_to_database(docker_conn_options) as conn:
        command_database(
            conn,
            "insert into rates (closingdate, currencysymbol, exchangerate)"
            "values (?, ?, ?)",
            [closing_date, currency_symbol, exchange_rate],
        )


if __name__ == "__main__":
    run()
