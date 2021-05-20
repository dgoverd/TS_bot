import os
from typing import Dict, List

import sqlite3


def ensure_connection(func):
    def wrapper(*args, **kwargs):
        with sqlite3.connect(os.path.join("db", "timesheets.db")) as conn:
            conn.execute("PRAGMA foreign_keys = 1")
            result = func(*args, conn=conn, **kwargs)
        return result

    return wrapper


@ensure_connection
def insert(conn, table: str, column_values: Dict) -> None:
    cursor = conn.cursor()
    columns = ', '.join(column_values.keys())
    values = [tuple(column_values.values())]
    placeholders = ", ".join("?" * len(column_values.keys()))
    cursor.executemany(
        f"INSERT OR IGNORE INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


@ensure_connection
def fetchall(conn, table: str, columns: List[str]) -> List[Dict[str, any]]:
    cursor = conn.cursor()
    columns_joined = ", ".join(columns)
    cursor.execute(f"SELECT {columns_joined} FROM {table}")
    rows = cursor.fetchall()
    result = []
    for row in rows:
        dict_row = {}
        for index, column in enumerate(columns):
            dict_row[column] = row[index]
        result.append(dict_row)
    return result


@ensure_connection
def delete(conn, table: str, row_id: int):
    cursor = conn.cursor()
    cursor.execute(f"delete from {table} where id={row_id}")
    conn.commit()


@ensure_connection
def get_cursor(conn):
    cursor = conn.cursor()
    return cursor


@ensure_connection
def _init_db(conn):
    with open("createdb.sql", "r") as f:
        sql = f.read()
    cursor = conn.cursor()
    cursor.executescript(sql)
    conn.commit()


@ensure_connection
def check_init_db(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master "
                   "WHERE type='table' AND name='Users'")
    table_exists = cursor.fetchall()
    if table_exists:
        return
    _init_db()
