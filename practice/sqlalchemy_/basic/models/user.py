import typing

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if typing.TYPE_CHECKING:
    from .post import Post

from .base import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False)
    fullname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    posts: Mapped[list['Post']] = relationship(back_populates='author')

    def __repr__(self) -> str:
        return (
            f'User(id={self.id!r}, '
            f'username={self.username!r}, '
            f'fullname={self.fullname!r}, '
            f'email={self.email!r})'
        )
