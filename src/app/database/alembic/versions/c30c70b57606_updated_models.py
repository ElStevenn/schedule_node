"""Updated models

Revision ID: c30c70b57606
Revises: a390ce7f5ddb
Create Date: 2024-12-03 16:17:55.302449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c30c70b57606'
down_revision: Union[str, None] = 'a390ce7f5ddb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('account_permissions', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accounts', 'account_permissions')
    # ### end Alembic commands ###
