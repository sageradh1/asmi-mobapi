"""Added Gender and CreatedTime for Users table

Revision ID: 33d7ff1455e0
Revises: d2768fd0dad0
Create Date: 2020-01-31 18:47:06.692632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33d7ff1455e0'
down_revision = 'd2768fd0dad0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('created_datetime', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('gender', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_created_datetime'), 'user', ['created_datetime'], unique=False)
    op.create_index(op.f('ix_user_gender'), 'user', ['gender'], unique=False)
    op.drop_index('ix_user_email', table_name='user')
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    op.drop_index(op.f('ix_user_gender'), table_name='user')
    op.drop_index(op.f('ix_user_created_datetime'), table_name='user')
    op.drop_column('user', 'gender')
    op.drop_column('user', 'created_datetime')
    # ### end Alembic commands ###
