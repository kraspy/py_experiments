from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String, Text, sql
from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel
from .post import Post
from .posts_tags import posts_tags_association

if TYPE_CHECKING:
    from .post import Post


class Tag(BaseModel):
    __tablename__ = 'tags'

    name: Mapped[int] = mapped_column(
        CITEXT(50),
        primary_key=True,
    )
    slug: Mapped[str] = mapped_column(
        String(60),
        unique=True,
    )
    description: Mapped[str] = mapped_column(
        Text,
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=sql.func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=sql.func.now(),
        onupdate=sql.func.now(),
    )
    posts: Mapped[list['Post']] = relationship(
        back_populates='tags',
        secondary=posts_tags_association,
    )
