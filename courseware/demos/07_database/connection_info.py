from typing import Generator, Any
from contextlib import contextmanager
import pyodbc

express_conn_options = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost\\SQLExpress;"
    "DATABASE=ratesapp;"
    "UID=sa;"
    "PWD=sqlDBp@ss!;"
    "Encrypt=no;"
)


docker_conn_options = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=ratesapp;"
    "UID=sa;"
    "PWD=sqlDBp@ss!;"
    "Encrypt=no;"
)


@contextmanager
def connect_to_database(
    conn_options: str
) -> Generator[pyodbc.Connection, None, None]:
    try:
        conn = pyodbc.connect(conn_options)
        yield conn
    finally:
        conn.close()


@contextmanager
def query_database(
    conn: pyodbc.Connection, query: str, params: list[Any] = []
) -> Generator[pyodbc.Cursor, None, None]:
    try:
        cursor = conn.execute(query, params)
        yield cursor
    finally:
        cursor.close()


def command_database(
    conn: pyodbc.Connection, query: str, params: list[Any] = []
) -> pyodbc.Cursor:
    try:
        cursor = conn.execute(query, params)
        cursor.commit()
    finally:
        cursor.close()


@contextmanager
def create_cursor(
    conn: pyodbc.Connection, autocommit: bool = True
) -> Generator[pyodbc.Cursor, None, None]:
    try:
        cursor = conn.cursor()
        yield cursor
        if autocommit:
            cursor.commit()
    finally:
        cursor.close()
