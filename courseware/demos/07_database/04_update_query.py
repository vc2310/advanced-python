""" params query """

from connection_info import (
    connect_to_database,
    command_database,
    docker_conn_options,
)


def run() -> None:
    """run"""

    closing_date = "2021-10-04"
    currency_symbol = "HKD"
    exchange_rate = 2.00

    with connect_to_database(docker_conn_options) as conn:
        command_database(
            conn,
            "update rates set closingdate = ?, currencysymbol = ?, "
            "exchangerate = ? where ratesid = ?",
            [closing_date, currency_symbol, exchange_rate, 5],
        )


if __name__ == "__main__":
    run()
