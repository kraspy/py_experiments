from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Identity, String, func, sql
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

if TYPE_CHECKING:
    from .post import Post


class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Identity(always=True),
        primary_key=True,
    )
    username: Mapped[str] = mapped_column(
        String(30),
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )
    is_active: Mapped[bool] = mapped_column(
        server_default=sql.true(),
    )
    profile: Mapped[dict] = mapped_column(
        JSONB,
        server_default='{}',
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        server_onupdate=func.now(),  # Проверить, обновляется ли без триггера в БД
    )
    posts: Mapped[list['Post']] = relationship(back_populates='author')
