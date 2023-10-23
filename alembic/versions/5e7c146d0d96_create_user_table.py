"""Create User Table

Revision ID: 5e7c146d0d96
Revises: d752e166c095
Create Date: 2023-10-23 23:34:44.550433

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5e7c146d0d96'
down_revision: Union[str, None] = 'd752e166c095'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(80), unique=True, nullable=False),
        sa.Column('password', sa.String(120), nullable=False),
        sa.Column('role', sa.String(80), nullable=False)
    )


def downgrade() -> None:
    pass
