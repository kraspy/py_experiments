from pathlib import Path

import psycopg as pg

BASE_DIR = Path(__file__).parent
QUERIES_DIR = BASE_DIR / 'queries'

DSN = 'dbname=postgres user=postgres password=password host=localhost port=5432'


def execute_sql(sql_filename, autocommit: bool):
    with pg.connect(DSN, autocommit=autocommit) as conn:
        with conn.cursor() as cur:
            with open(QUERIES_DIR / (sql_filename + '.sql')) as f:
                sql = f.read()
            print(cur.execute(sql))
