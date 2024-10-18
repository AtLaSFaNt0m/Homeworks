"""Initial migration

Revision ID: 0978ad647b04
Revises: 
Create Date: 2024-10-18 18:46:37.369222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0978ad647b04'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tasks', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('tasks', 'content',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'firstname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'lastname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'firstname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('tasks', 'content',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('tasks', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
