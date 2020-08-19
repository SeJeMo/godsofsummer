"""added season goals

Revision ID: ff36120fad6b
Revises: 485a287505a7
Create Date: 2020-08-19 16:20:27.715923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff36120fad6b'
down_revision = '485a287505a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('season_goals', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'season_goals')
    # ### end Alembic commands ###
