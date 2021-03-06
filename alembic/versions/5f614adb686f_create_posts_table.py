"""create posts table

Revision ID: 5f614adb686f
Revises: 
Create Date: 2021-12-05 12:57:32.183048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f614adb686f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))

    pass

def downgrade():
    op.drop_table('posts')
    pass
