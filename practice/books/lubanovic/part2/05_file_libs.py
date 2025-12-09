import csv
from pathlib import Path
import sqlite3
import sqlalchemy as sa
import redis

BASE_DIR = Path(__file__).parent

# 16.1
data = [
    ['author', 'book'],
    ['J R R Tolkien', 'The Hobbit'],
    ['Lynne Truss', 'Eats, Shoots & Leaves'],
]

print('--- 16.1 ---')
with open(BASE_DIR / 'books.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 16.2
print('--- 16.2 ---')
with open(BASE_DIR / 'books.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 16.3
print('--- 16.3 ---')
data = [
    ['title', 'author', 'year'],
    ['The Weirdstone of Brisingamen', 'Alan Garner', 1960],
    ['Perdido Street Station', 'China Miéville', 2000],
    ['Thud!', 'Terry Pratchett', 2005],
    ['The Spellman Files', 'Lisa Lutz', 2007],
    ['Small Gods', 'Terry Pratchett', 1992],
]

with open(BASE_DIR / 'books.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 16.4
print('--- 16.4 ---')
with sqlite3.connect(BASE_DIR / 'books.db') as conn:
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS books')
    cursor.execute('CREATE TABLE books (title TEXT, author TEXT, year INT)')

# 16.5
print('--- 16.5 ---')
with open(BASE_DIR / 'books.csv', 'r') as f:
    reader = csv.DictReader(f)

    with sqlite3.connect(BASE_DIR / 'books.db') as conn:
        cursor = conn.cursor()
        cursor.executemany('INSERT INTO books VALUES (:title, :author, :year)', reader)
        conn.commit()

# 16.6
print('--- 16.6 ---')
with sqlite3.connect(BASE_DIR / 'books.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT title FROM books ORDER BY title ASC')
    for row in cursor:
        print(row[0])

# 16.7
print('--- 16.7 ---')
with sqlite3.connect(BASE_DIR / 'books.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM books ORDER BY year ASC')
    for row in cursor:
        print(row)

# 16.8
print('--- 16.8 ---')
engine = sa.create_engine(f'sqlite:///{BASE_DIR / "books.db"}')
with engine.connect() as conn:
    result = conn.execute(
        sa.text('SELECT title FROM books ORDER BY title ASC'),
    )
    for row in result:
        print(row)

# 16.9
print('--- 16.9 ---')
conn = redis.Redis()
print(conn.keys('*'))

conn.hset('test', mapping={'count': 1, 'name': 'Fester Bestertester'})
print(conn.hgetall('test'))

# 16.10
print('--- 16.10 ---')
conn.hincrby('test', 'count')
print(conn.hgetall('test'))
