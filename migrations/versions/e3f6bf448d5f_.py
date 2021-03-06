"""empty message

Revision ID: e3f6bf448d5f
Revises: c4665b8d682b
Create Date: 2019-12-26 14:40:14.721193

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e3f6bf448d5f'
down_revision = 'c4665b8d682b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goods', sa.Column('price', sa.String(length=5), nullable=True))
    op.drop_column('goods', 'gprice')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goods', sa.Column('gprice', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_column('goods', 'price')
    # ### end Alembic commands ###
