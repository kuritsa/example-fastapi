"""add content column to posts table

Revision ID: 015bfbd6a88e
Revises: 5f614adb686f
Create Date: 2021-12-05 13:09:29.393241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '015bfbd6a88e'
down_revision = '5f614adb686f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
