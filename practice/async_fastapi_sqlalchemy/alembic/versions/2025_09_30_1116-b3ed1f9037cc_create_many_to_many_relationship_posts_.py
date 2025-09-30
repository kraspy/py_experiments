"""create Many-To_Many relationship (posts <-> tags)

Revision ID: b3ed1f9037cc
Revises: 6c71b2a02a8b
Create Date: 2025-09-30 11:16:55.791925

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b3ed1f9037cc'
down_revision: Union[str, Sequence[str], None] = '6c71b2a02a8b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute('CREATE EXTENSION IF NOT EXISTS citext')
    op.create_table(
        'tags',
        sa.Column(
            'name',
            postgresql.CITEXT(length=50),
            nullable=False,
        ),
        sa.Column(
            'slug',
            sa.String(length=60),
            nullable=False,
        ),
        sa.Column(
            'description',
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            'created_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint('name'),
        sa.UniqueConstraint('slug'),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute('DROP EXTENSION IF EXISTS citext')
    op.drop_table('tags')
