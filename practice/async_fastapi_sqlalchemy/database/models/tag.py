from datetime import datetime

from sqlalchemy import DateTime, String, Text, sql
from sqlalchemy.dialects.postgresql import CITEXT
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseModel


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
