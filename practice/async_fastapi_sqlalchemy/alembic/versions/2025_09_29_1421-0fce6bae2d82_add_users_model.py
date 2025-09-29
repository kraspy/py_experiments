"""add Users model

Revision ID: 0fce6bae2d82
Revises:
Create Date: 2025-09-29 14:21:32.730242

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0fce6bae2d82'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), sa.Identity(always=True), nullable=False),
        sa.Column('username', sa.String(length=30), nullable=False),
        sa.Column('email', sa.String(length=150), nullable=False),
        sa.Column('full_name', sa.String(length=150), nullable=True),
        sa.Column(
            'is_active', sa.Boolean(), server_default=sa.text('true'), nullable=False
        ),
        sa.Column(
            'profile',
            postgresql.JSONB(astext_type=sa.Text()),
            server_default='{}',
            nullable=False,
        ),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.Column(
            'updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False
        ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
