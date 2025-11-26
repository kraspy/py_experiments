import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_FILE = BASE_DIR / 'db.sqlite3'


# ========================================
# Functions
# ========================================
def truncate_database(conn: sqlite3.Connection):
    cur = conn.cursor()
    stmt = """
    DROP TABLE IF EXISTS inventory;
    DROP TABLE IF EXISTS employees;
    DROP TABLE IF EXISTS sales;
    """

    cur.executescript(stmt)

    cur.close()


def create_tables(conn: sqlite3.Connection):
    cur = conn.cursor()
    stmt = """
        CREATE TABLE inventory (
            item_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            price REAL,
            PRIMARY KEY (item_id)
        );

        CREATE TABLE employees (
            employee_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            PRIMARY KEY (employee_id)
        );

        CREATE TABLE sales (
            sale_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            region TEXT NOT NULL,
            amount REAL NOT NULL,
            sale_date TEXT NOT NULL,
            PRIMARY KEY (sale_id)
        );
        """

    cur.executescript(stmt)

    cur.close()


def insert_inventory_data(conn: sqlite3.Connection, data: list[tuple]):
    cur = conn.cursor()
    stmt = """
    INSERT INTO inventory (name, price)
    VALUES (?, ?);
    """

    cur.executemany(stmt, data)

    cur.close()


def insert_employees_data(conn: sqlite3.Connection, data: list[tuple]):
    cur = conn.cursor()
    stmt = """
    INSERT INTO employees (name, position)
    VALUES (?, ?);
    """

    cur.executemany(stmt, data)

    cur.close()


def insert_sales_data(conn: sqlite3.Connection):
    stmt = """
    INSERT INTO sales (product_id, region, amount, sale_date)
    VALUES (1, 'North', 150.75, '2025-11-26'),
           (2, 'South', 230.50, '2025-11-25'),
           (3, 'East', 99.99, '2025-11-26'),
           (1, 'West', 400.00, '2025-11-26'),
           (4, 'Central', 75.25, '2025-11-24'),
           (2, 'North', 120.00, '2025-11-26'),
           (3, 'South', 300.00, '2025-11-24'),
           (4, 'East', 50.00, '2025-11-25');
    """
    cur = conn.cursor()
    cur.execute(stmt)

    cur.close()


def add_sql_injection(conn: sqlite3.Connection):
    cur = conn.cursor()
    sql_injection = "'Item 4', 40.0); DROP TABLE inventory; --"

    stmt = f'INSERT INTO inventory (name, price) VALUES ({sql_injection}, 40.0);'

    cur.executescript(stmt)

    cur.close()


def get_inventory_with_price_more_than(conn: sqlite3.Connection, price: float):
    cur = conn.cursor()
    stmt = """
    SELECT * FROM inventory WHERE price > ?;
    """

    cur.execute(stmt, (price,))

    row = cur.fetchone()

    while row:
        print(f'{row[1]:<10}{row[2]:>10}')
        row = cur.fetchone()

    cur.close()


def get_aggregated_sales_data(conn: sqlite3.Connection):
    cur = conn.cursor()
    stmt = """
    SELECT sale_date, COUNT(*) as total_sales FROM sales GROUP BY sale_date;
    """

    cur.execute(stmt)

    row = cur.fetchall()

    print(row)
    cur.close()


def get_employees(conn: sqlite3.Connection):
    cur = conn.cursor()
    stmt = """
    SELECT * FROM employees;
    """

    cur.execute(stmt)

    row = cur.fetchall()

    print(row)
    cur.close()


def get_employee_by_id(conn: sqlite3.Connection, employee_id: int):
    cur = conn.cursor()
    stmt = """
    SELECT * FROM employees WHERE employee_id = ?;
    """

    cur.execute(stmt, (employee_id,))

    row = cur.fetchone()

    print(row)
    cur.close()


def edit_employee_position(
    conn: sqlite3.Connection,
    employee_id: int,
    position: str,
):
    cur = conn.cursor()
    stmt = """
    UPDATE employees SET position = ? WHERE employee_id = ?;
    """

    cur.execute(stmt, (position, employee_id))

    cur.close()


def delete_employee_by_id(conn: sqlite3.Connection, employee_id: int):
    cur = conn.cursor()
    stmt = """
    DELETE FROM employees WHERE employee_id = ?;
    """

    cur.execute(stmt, (employee_id,))

    cur.close()


# ========================================
# Main
# ========================================
def main():
    with sqlite3.connect(DB_FILE) as conn:
        truncate_database(conn)
        create_tables(conn)

        inventory_data = [
            ('Item 1', 10.0),
            ('Item 2', 20.0),
            ('Item 3', 30.0),
        ]

        insert_inventory_data(conn, inventory_data)

        insert_sales_data(conn)

        employees_data = [
            ('Employee 1', 'SEO'),
            ('Employee 2', 'Frontend'),
            ('Employee 3', 'Backend'),
        ]

        insert_employees_data(conn, employees_data)

        # add_sql_injection(conn)

        get_inventory_with_price_more_than(conn, 15)
        get_aggregated_sales_data(conn)

        get_employees(conn)
        edit_employee_position(conn, 1, 'ML Developer')
        delete_employee_by_id(conn, 2)
        get_employees(conn)


if __name__ == '__main__':
    main()
