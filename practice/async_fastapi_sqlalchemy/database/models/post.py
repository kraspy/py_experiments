from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Identity,
    Index,
    String,
    Text,
    sql,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseModel

if TYPE_CHECKING:
    from .user import User


class Post(BaseModel):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(
        Identity(always=True),
        primary_key=True,
    )
    author_id: Mapped[int] = mapped_column(
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
    )
    author: Mapped['User'] = relationship(
        back_populates='posts',
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    is_published: Mapped[bool] = mapped_column(
        Boolean,
        server_default=sql.false(),
    )
    published_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
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

    __table_args__ = (
        Index(
            'ix_author_id_created_at',
            'author_id',
            'created_at',
        ),
        CheckConstraint(
            'is_published = false OR published_at IS NOT NULL',
            name='check_is_published',
        ),
    )


Index(
    'ix_is_published_published_at',
    Post.is_published,
    Post.published_at,
    postgresql_where=Post.is_published.is_(True),
)
