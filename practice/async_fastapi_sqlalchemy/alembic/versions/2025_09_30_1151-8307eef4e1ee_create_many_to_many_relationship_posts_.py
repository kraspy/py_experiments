"""create Many-To_Many relationship (posts <-> tags)

Revision ID: 8307eef4e1ee
Revises: b3ed1f9037cc
Create Date: 2025-09-30 11:51:12.495575

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '8307eef4e1ee'
down_revision: Union[str, Sequence[str], None] = 'b3ed1f9037cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        'posts_tags',
        sa.Column('post_id', sa.Integer(), nullable=False),
        sa.Column('tag_name', postgresql.CITEXT(), nullable=False),
        sa.ForeignKeyConstraint(
            ['post_id'],
            ['posts.id'],
        ),
        sa.ForeignKeyConstraint(
            ['tag_name'],
            ['tags.name'],
        ),
        sa.PrimaryKeyConstraint('post_id', 'tag_name'),
    )
    op.create_index('ix_tag_name', 'posts_tags', ['tag_name'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('ix_tag_name', table_name='posts_tags')
    op.drop_table('posts_tags')
