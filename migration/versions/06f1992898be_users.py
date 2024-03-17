"""users

Revision ID: 06f1992898be
Revises: e52018bdbad7
Create Date: 2024-02-20 23:54:33.510673

"""
from typing import Sequence, Union
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table, Enum
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06f1992898be'
down_revision: Union[str, None] = 'e52018bdbad7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
        Column('id', Integer(), primary_key=True),
        Column('name', String(), nullable=False),
        Column('email', String(length=255), nullable=False, unique=True),
        Column('password', DateTime, nullable=False),
        Column('role', Enum('chef', 'su_chef', 'cook',name = 'role'), nullable= False),
                )


def downgrade() -> None:
    op.drop_table('users')
