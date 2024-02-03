"""create client_order table

Revision ID: 52bd5de529e6
Revises: 1a9343440bef
Create Date: 2024-02-03 22:47:37.913665

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52bd5de529e6'
down_revision: Union[str, None] = '1a9343440bef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('client_order',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('client_id', sa.Integer(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('deleted_at', sa.DateTime(), nullable=False),
                    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('client_order')
