from _db import DB_FILE, create_database, fill_mock_data
import sqlite3
from typing import Callable


# ========================================
# Utils
# ========================================
def print_taskname(tsk: Callable) -> None:
    def wrapper() -> None:
        print(f'\nTask: {tsk.__name__}')
        tsk()

    return wrapper


# ========================================
# Tasks
# ========================================


@print_taskname
def task_1() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM stocks;')
        rows = cursor.fetchall()
        for row in rows:
            print(row)


@print_taskname
def task_2() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT TradingSymbol FROM stocks;')
        rows = cursor.fetchall()
        for row in rows:
            print(row)


@print_taskname
def task_3() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT TradingSymbol, NumShares FROM stocks;')
        rows = cursor.fetchall()
        for row in rows:
            print(row)


@print_taskname
def task_4() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT TradingSymbol
            FROM stocks 
            WHERE PurchasePrice > 1000;"""
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)


@print_taskname
def task_5() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT *
            FROM stocks 
            WHERE TradingSymbol LIKE 'GO%';"""
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)


@print_taskname
def task_6() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT TradingSymbol
            FROM stocks 
            WHERE PurchasePrice > SellingPrice AND NumShares > 100;"""
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)


@print_taskname
def task_7() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """SELECT TradingSymbol, NumShares
            FROM stocks 
            WHERE SellingPrice > PurchasePrice AND NumShares > 50
            ORDER BY NumShares;"""
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)


@print_taskname
def task_8() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO 
                stocks (TradingSymbol, CompanyName, NumShares, PurchasePrice, SellingPrice)
            VALUES
                ('XYZ', 'Компания XYZ', 150, 12.55, 22.47);"""
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        for row in cursor.execute('SELECT * FROM stocks;'):
            print(row)


@print_taskname
def task_9() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """UPDATE stocks 
            SET TradingSymbol = 'ABC'
            WHERE TradingSymbol = 'XYZ';"""
        )
        rows = cursor.fetchall()
        for row in rows:
            print(row)

        for row in cursor.execute('SELECT * FROM stocks;'):
            print(row)


@print_taskname
def task_10() -> None:
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """DELETE FROM stocks 
            WHERE NumShares > 100;"""
        )

        for row in cursor.execute('SELECT * FROM stocks;'):
            print(row)


# ========================================
# Main
# ========================================
def main() -> None:
    create_database()
    fill_mock_data()

    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()
    task_7()
    task_8()
    task_9()
    task_10()


if __name__ == '__main__':
    main()
