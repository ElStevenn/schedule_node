"""Updated models

Revision ID: 76dd0436c560
Revises: 14a7ed7c7e6b
Create Date: 2024-10-08 15:48:17.709733

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76dd0436c560'
down_revision: Union[str, None] = '14a7ed7c7e6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_credentials',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('account_id', sa.String(length=255), nullable=False),
    sa.Column('encrypted_apikey', sa.LargeBinary(), nullable=False),
    sa.Column('encrypted_secret_key', sa.LargeBinary(), nullable=False),
    sa.Column('encrypted_passphrase', sa.LargeBinary(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_credentials')
    # ### end Alembic commands ###