"""create users table

Revision ID: fdf8f910ed13
Revises:
Create Date: 2025-09-24 11:36:04.703863

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = 'fdf8f910ed13'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column(
            'id',
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            'username',
            sa.String(length=20),
            nullable=False,
        ),
        sa.Column(
            'fullname',
            sa.String(length=50),
            nullable=False,
        ),
        sa.Column(
            'email',
            sa.String(length=120),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
