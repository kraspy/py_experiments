import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).parent
DB_FILE = BASE_DIR / 'db.sqlite3'


def create_database() -> bool:
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.executescript("""
                DROP TABLE IF EXISTS stocks;
                CREATE TABLE IF NOT EXISTS stocks (
                    TradingSymbol TEXT,
                    CompanyName TEXT,
                    NumShares INTEGER,
                    PurchasePrice REAL,
                    SellingPrice REAL
                );
            """)
            cursor.close()
        return True
    except sqlite3.Error as e:
        print(f'Ошибка при создании базы данных: {e}')
        return False


def fill_mock_data() -> bool:
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO stocks (TradingSymbol, CompanyName, NumShares, PurchasePrice, SellingPrice)
                VALUES
                ('AAPL', 'Apple Inc.', 100, 150.75, 160.25),
                ('MSFT', 'Microsoft Corporation', 50, 250.50, 260.75),
                ('GOOGL', 'Alphabet Inc.', 75, 1200.00, 1250.25),
                ('AMZN', 'Amazon.com, Inc.', 150, 3500.50, 3100.75),
                ('FB', 'Facebook, Inc.', 200, 350.25, 360.50)
            """)
            cursor.close()
        return True
    except sqlite3.Error as e:
        print(f'Ошибка при заполнении базы данных: {e}')
        return False


if __name__ == '__main__':
    if create_database():
        print('База данных создана успешно')
    else:
        print('Ошибка при создании базы данных')

    if fill_mock_data():
        print('Данные заполнены успешно')
    else:
        print('Ошибка при заполнении базы данных')
