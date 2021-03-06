"""user settings

Revision ID: e7d5e11363b0
Revises: 01b14c0b630c
Create Date: 2020-08-19 13:41:16.447760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7d5e11363b0'
down_revision = '01b14c0b630c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('avatar', sa.String(length=256), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_settings_username'), 'settings', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_settings_username'), table_name='settings')
    op.drop_table('settings')
    # ### end Alembic commands ###
