"""empty message

Revision ID: 85b4488d74fb
Revises: e3f6bf448d5f
Create Date: 2019-12-26 14:41:30.592091

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '85b4488d74fb'
down_revision = 'e3f6bf448d5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goods', sa.Column('gprice', sa.String(length=5), nullable=True))
    op.drop_column('goods', 'price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goods', sa.Column('price', mysql.VARCHAR(length=5), nullable=True))
    op.drop_column('goods', 'gprice')
    # ### end Alembic commands ###