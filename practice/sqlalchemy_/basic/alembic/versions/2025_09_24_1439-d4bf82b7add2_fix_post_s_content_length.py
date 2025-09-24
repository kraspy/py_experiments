"""fix post's content length

Revision ID: d4bf82b7add2
Revises: 7e3c168e9b6b
Create Date: 2025-09-24 14:39:52.869670

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = 'd4bf82b7add2'
down_revision: Union[str, Sequence[str], None] = '7e3c168e9b6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column(
        'posts',
        'content',
        existing_type=sa.VARCHAR(length=100),
        type_=sa.Text(),
        existing_nullable=False,
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column(
        'posts',
        'content',
        existing_type=sa.Text(),
        type_=sa.VARCHAR(length=100),
        existing_nullable=False,
    )
