"""create flient table

Revision ID: 1a9343440bef
Revises: cf9b6f7e717e
Create Date: 2024-02-03 22:45:55.038163

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a9343440bef'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('client',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(
                        length=255), nullable=False),
                    sa.Column('last_name', sa.String(
                        length=255), nullable=False),
                    sa.Column('password', sa.String(
                        length=255), nullable=False),
                    sa.Column('email', sa.String(length=255), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )


def downgrade() -> None:
    op.drop_table('client')
