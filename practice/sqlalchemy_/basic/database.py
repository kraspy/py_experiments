import os

import faker
from dotenv import load_dotenv
from models import Post, User
from sqlalchemy import create_engine, delete, insert, select, update
from sqlalchemy.orm import Session as SessionType
from sqlalchemy.orm import joinedload, selectinload, sessionmaker

load_dotenv()

pg_url = os.getenv('PG_URL') or 'postgresql://postgres:postgres@localhost:5432/postgres'

engine = create_engine(
    pg_url,
    echo=True,
)

session = sessionmaker(
    engine,
    expire_on_commit=False,  # Если True - После коммита объекты сессии просрачиваются (нужно делать новый запрос)
)


# ========================================
# region CREATE functions
# ========================================


def create_random_user():
    fkr = faker.Faker()
    return User(
        username=fkr.user_name(),
        fullname=fkr.name(),
        email=fkr.email(),
    )


def create_random_post(user: User):
    fkr = faker.Faker()
    return Post(
        title=fkr.sentence(),
        content=fkr.text(),
        author_id=user.id,
    )


def fill_database(session: SessionType, num_users: int = 10, num_posts: int = 10):
    import random

    users = [create_random_user() for _ in range(num_users)]
    for user in users:
        session.add(user)  # ADD ONE VALUE
        session.flush()

    posts = [create_random_post(user) for user in random.choices(users, k=num_posts)]
    session.add_all(posts)  # ADD ALL VALUES
    session.flush()

    session.commit()


# endregion
# ========================================


# ========================================
# region READ functions
# ========================================


def get_all_users(session: SessionType):
    return session.scalars(select(User)).all()


def get_user_with_posts(session: SessionType, user_id: int):
    user = session.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if not user:
        return None
    return user


def get_posts(session: SessionType):
    posts = session.scalars(select(Post)).all()

    return posts


def get_users_lazy(session: SessionType):  # Ленивая загрузка
    # N+1 (Неэффективен при большом количестве связаных данных)
    users = session.scalars(select(User)).all()

    return users


def get_users_joinedload(session: SessionType):  # LEFT JOIN с постобработкой
    # Многие к одному
    users = session.scalars(select(User).options(joinedload(User.posts))).unique().all()

    return users


def get_users_selectinload(session: SessionType):  # SELECT IN с постобработкой
    # Один ко многим / Многие ко многим
    users = session.scalars(select(User).options(selectinload(User.posts))).all()

    return users


# endregion
# ========================================
