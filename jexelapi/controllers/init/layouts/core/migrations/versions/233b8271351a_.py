"""empty message

Revision ID: 233b8271351a
Revises: 
Create Date: 2025-01-04 17:01:26.101668

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '233b8271351a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('path', sa.String(), nullable=False),
    sa.Column('ext', sa.String(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('folder', sa.String(), nullable=False),
    sa.Column('created_by', sa.UUID(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_files_id'), 'files', ['id'], unique=True)
    op.create_table('users',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=True),
    sa.Column('last_name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_uuid'), 'users', ['uuid'], unique=True)
    op.create_table('active_session',
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('firebase_token', sa.String(), nullable=True),
    sa.Column('user_uuid', sa.UUID(), nullable=True),
    sa.Column('expire_at', sa.DateTime(), nullable=False),
    sa.Column('logout_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_uuid'], ['users.uuid'], ),
    sa.PrimaryKeyConstraint('token')
    )
    op.create_index(op.f('ix_active_session_token'), 'active_session', ['token'], unique=True)
    op.create_index(op.f('ix_active_session_user_uuid'), 'active_session', ['user_uuid'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_active_session_user_uuid'), table_name='active_session')
    op.drop_index(op.f('ix_active_session_token'), table_name='active_session')
    op.drop_table('active_session')
    op.drop_index(op.f('ix_users_uuid'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_files_id'), table_name='files')
    op.drop_table('files')
    # ### end Alembic commands ###
