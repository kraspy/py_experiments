import os

from dotenv import load_dotenv

load_dotenv()


PG_URL = os.getenv('PG_URL')
