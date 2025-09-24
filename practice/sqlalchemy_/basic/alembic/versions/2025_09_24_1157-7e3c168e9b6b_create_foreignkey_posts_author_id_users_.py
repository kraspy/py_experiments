"""create ForeignKey: posts.author_id -> users.id

Revision ID: 7e3c168e9b6b
Revises: 12bfc769bef7
Create Date: 2025-09-24 11:57:56.057405

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = '7e3c168e9b6b'
down_revision: Union[str, Sequence[str], None] = '12bfc769bef7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'posts',
        sa.Column(
            'author_id',
            sa.Integer(),
            nullable=False,
        ),
    )
    op.create_foreign_key(
        None,
        'posts',
        'users',
        ['author_id'],
        ['id'],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'author_id')
