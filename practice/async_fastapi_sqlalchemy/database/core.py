from settings import PG_URL
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

async_engine = create_async_engine(
    url=PG_URL,
    echo=True,
)

async_session = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
)
