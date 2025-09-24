"""create posts table

Revision ID: 12bfc769bef7
Revises: fdf8f910ed13
Create Date: 2025-09-24 11:55:39.827531

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = '12bfc769bef7'
down_revision: Union[str, Sequence[str], None] = 'fdf8f910ed13'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'posts',
        sa.Column(
            'id',
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            'title',
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            'content',
            sa.String(length=100),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
