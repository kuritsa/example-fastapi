"""add foreign key to posts table

Revision ID: 07d19cb0421d
Revises: 898cd6118472
Create Date: 2021-12-05 13:24:03.401539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07d19cb0421d'
down_revision = '898cd6118472'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
