"""Updated models

Revision ID: 590ca31f14cd
Revises: c2e9c3e3fd11
Create Date: 2024-12-08 16:20:45.846527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '590ca31f14cd'
down_revision: Union[str, None] = 'c2e9c3e3fd11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###