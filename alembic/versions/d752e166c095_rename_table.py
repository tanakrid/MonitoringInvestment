"""rename_table

Revision ID: d752e166c095
Revises: 84697b71a126
Create Date: 2023-10-13 22:55:43.921458

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd752e166c095'
down_revision: Union[str, None] = '84697b71a126'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table('account', 'goal')


def downgrade() -> None:
    pass
