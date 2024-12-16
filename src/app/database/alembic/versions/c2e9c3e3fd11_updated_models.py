"""
Updated models

Revision ID: c2e9c3e3fd11
Revises: ce467f3970ee
Create Date: 2024-12-08 16:17:47.705143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c2e9c3e3fd11'
down_revision: Union[str, None] = 'ce467f3970ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'accounts', 
        'account_permissions',
        existing_type=sa.VARCHAR(length=255),
        type_=postgresql.JSON(astext_type=sa.Text()),
        existing_nullable=True,
        postgresql_using="account_permissions::json"  # Add the USING clause
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        'accounts', 
        'account_permissions',
        existing_type=postgresql.JSON(astext_type=sa.Text()),
        type_=sa.VARCHAR(length=255),
        existing_nullable=True,
        postgresql_using="account_permissions::text"  # Reverse the conversion for downgrade
    )
    # ### end Alembic commands ###