"""initial migration

Revision ID: 84697b71a126
Revises: 
Create Date: 2023-10-13 17:48:06.180481

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84697b71a126'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(120), nullable=False),
        sa.Column('target', sa.Integer, nullable=False),
        sa.Column('start_date', sa.String(120), nullable=False),
        sa.Column('end_date', sa.String(120), nullable=False),
        sa.Column('progress', sa.Float, nullable=False),
    )


def downgrade() -> None:
    pass
