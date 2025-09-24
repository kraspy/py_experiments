import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

pg_url = os.getenv('PG_URL') or 'postgresql://postgres:postgres@localhost:5432/postgres'

engine = create_engine(
    pg_url,
    echo=True,
)

session = sessionmaker(
    engine,
    expire_on_commit=False,
)
