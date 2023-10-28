"""create CashFLowStatement table

Revision ID: 599391f5df18
Revises: d5495d7f55e8
Create Date: 2023-10-29 00:39:09.871492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '599391f5df18'
down_revision: Union[str, None] = 'd5495d7f55e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('CashFlowStatements',
    sa.Column('id', sa.INTEGER, autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.String(length=120), nullable=False),
    sa.Column('update_date', sa.String(length=120), nullable=True),
    sa.Column('del_date', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )

def downgrade() -> None:
    pass
