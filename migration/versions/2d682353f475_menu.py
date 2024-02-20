"""menu

Revision ID: 2d682353f475
Revises: 06f1992898be
Create Date: 2024-02-20 23:58:17.745506

"""
from typing import Sequence, Union
from sqlalchemy import Column, Integer, String, Text, ForeignKeyConstraint, DateTime, Table, Enum
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d682353f475'
down_revision: Union[str, None] = '06f1992898be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table(
          'menu',
          Column('id', Integer(), primary_key = True),
          Column('name', String(), nullable = False),
          Column('prize', Integer(), nullable = False),
          Column('weight(g)', Integer(), nullable = False),
          Column('kcal', Integer(), nullable = False),
          Column('user_id', Integer(), nullable= False),
          Column('client_order_id', Integer(), nullable= False),
          ForeignKeyConstraint(['user_id'], ['users.id'],),
          ForeignKeyConstraint(['client_order_id'], ['client_order.id'],),

     )


def downgrade() -> None:
    op.drop_table('menu')
