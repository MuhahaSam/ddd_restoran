"""menu_ingredient

Revision ID: d03af00643f0
Revises: 2d682353f475
Create Date: 2024-02-21 00:10:57.349054

"""
from typing import Sequence, Union
from sqlalchemy import Column, Integer, String, Text, ForeignKeyConstraint, DateTime, Table, Enum
from alembic import op
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd03af00643f0'
down_revision: Union[str, None] = '2d682353f475'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'menu_ingredient',
        Column('id', Integer(), primary_key=True),
        Column('store_ingredient_id', Integer(), nullable = False),
        Column('weight', Integer(), nullable = False),
        Column('menu_id', Integer(), nullable = False),
        ForeignKeyConstraint(['store_ingredient_id'], ['store_ingredient.id']),
        ForeignKeyConstraint(['menu_id'], ['menu.id']),
    )


def downgrade() -> None:
    op.drop_table('menu_ingredient')
