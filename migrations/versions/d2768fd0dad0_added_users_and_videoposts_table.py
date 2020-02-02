"""Added Users and VideoPosts table

Revision ID: d2768fd0dad0
Revises: 
Create Date: 2020-01-31 17:51:13.504762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2768fd0dad0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('_phone_number', sa.Unicode(length=255), nullable=True),
    sa.Column('phone_country_code', sa.Unicode(length=8), nullable=True),
    sa.Column('date_of_birth', sa.DateTime(), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_date_of_birth'), 'user', ['date_of_birth'], unique=False)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_first_name'), 'user', ['first_name'], unique=False)
    op.create_index(op.f('ix_user_last_name'), 'user', ['last_name'], unique=False)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('video_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=100), nullable=True),
    sa.Column('extension', sa.String(length=5), nullable=True),
    sa.Column('storagelocation', sa.String(length=500), nullable=True),
    sa.Column('upload_started_time', sa.DateTime(), nullable=True),
    sa.Column('upload_completed_time', sa.DateTime(), nullable=True),
    sa.Column('last_modified_time', sa.DateTime(), nullable=True),
    sa.Column('caption', sa.String(length=440), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('filename')
    )
    op.create_index(op.f('ix_video_post_last_modified_time'), 'video_post', ['last_modified_time'], unique=False)
    op.create_index(op.f('ix_video_post_upload_completed_time'), 'video_post', ['upload_completed_time'], unique=False)
    op.create_index(op.f('ix_video_post_upload_started_time'), 'video_post', ['upload_started_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_video_post_upload_started_time'), table_name='video_post')
    op.drop_index(op.f('ix_video_post_upload_completed_time'), table_name='video_post')
    op.drop_index(op.f('ix_video_post_last_modified_time'), table_name='video_post')
    op.drop_table('video_post')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_last_name'), table_name='user')
    op.drop_index(op.f('ix_user_first_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_index(op.f('ix_user_date_of_birth'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
