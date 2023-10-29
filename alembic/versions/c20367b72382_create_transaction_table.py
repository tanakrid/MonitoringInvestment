"""create transaction table

Revision ID: c20367b72382
Revises: 599391f5df18
Create Date: 2023-10-29 03:02:39.789750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c20367b72382'
down_revision: Union[str, None] = '599391f5df18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('transactions',
        sa.Column('id', sa.INTEGER, autoincrement=True, nullable=False),
        sa.Column('tran_type', sa.String(length=80), nullable=False),
        sa.Column('desc', sa.String(length=120), nullable=True),
        sa.Column('amount', sa.Float, nullable=False),
        sa.Column('catagory_type', sa.String(length=120), nullable=False),
        sa.Column('custom_catagory_type', sa.String(length=120), nullable=True),
        sa.Column('create_date', sa.String(length=120), nullable=False),
        sa.Column('update_date', sa.String(length=120), nullable=True),
        sa.Column('del_date', sa.String(length=120), nullable=True),
        sa.Column('cash_flow_id', sa.INTEGER, nullable=False),
        sa.ForeignKeyConstraint(['cash_flow_id'], ['cash_flow_statements.id'], ),
        sa.PrimaryKeyConstraint('id'),
        mysql_collate='utf8mb4_0900_ai_ci',
        mysql_default_charset='utf8mb4',
        mysql_engine='InnoDB'
    )


def downgrade() -> None:
    pass
