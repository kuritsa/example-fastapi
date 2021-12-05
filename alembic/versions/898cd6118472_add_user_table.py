"""add user table

Revision ID: 898cd6118472
Revises: 015bfbd6a88e
Create Date: 2021-12-05 13:14:06.774769

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '898cd6118472'
down_revision = '015bfbd6a88e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
