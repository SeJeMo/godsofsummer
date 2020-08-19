"""new fields in user

Revision ID: 485a287505a7
Revises: e7d5e11363b0
Create Date: 2020-08-19 15:55:07.870154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '485a287505a7'
down_revision = 'e7d5e11363b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=256), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
