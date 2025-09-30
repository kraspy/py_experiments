from sqlalchemy import Column, ForeignKey, Index, Integer, PrimaryKeyConstraint, Table
from sqlalchemy.dialects.postgresql import CITEXT

from .base import BaseModel

posts_tags_association = Table(
    'posts_tags',
    BaseModel.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_name', CITEXT, ForeignKey('tags.name')),
    PrimaryKeyConstraint('post_id', 'tag_name'),
    Index('ix_tag_name', 'tag_name'),
)
