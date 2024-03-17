"""store_ingredient

Revision ID: e52018bdbad7
Revises: 52bd5de529e6
Create Date: 2024-02-20 23:49:00.012164

"""
from typing import Sequence, Union
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Table
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e52018bdbad7'
down_revision: Union[str, None] = '52bd5de529e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('store_ingredient',
        Column('id', Integer(), primary_key=True),
        Column('name', String(), nullable=False),
        Column('prize', Integer(), nullable=False),
        Column('where_from', String(), nullable=False),
        Column('order_date', DateTime(), nullable=False),
        Column('expiration_day', Integer(), nullable=False), #how many day left
        Column('inventory', Integer(), nullable=False),
                )


def downgrade() -> None:
    op.drop_table('store_ingredient')
