"""Updated models

Revision ID: 423e1fc52648
Revises: 9523b1ef1ff4
Create Date: 2024-12-30 12:31:50.709720

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '423e1fc52648'
down_revision: Union[str, None] = '9523b1ef1ff4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('futures_history',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('account_id', sa.String(length=255), nullable=False),
    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
    sa.Column('asset', sa.String(length=255), nullable=False),
    sa.Column('balance', sa.Float(), nullable=False),
    sa.Column('usd_value', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.account_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spot_history',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('account_id', sa.String(length=255), nullable=False),
    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=False),
    sa.Column('asset', sa.String(length=255), nullable=False),
    sa.Column('balance', sa.Float(), nullable=False),
    sa.Column('usd_value', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.account_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('crypto_historical_pnl')
    op.drop_table('future_cryptos')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('future_cryptos',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('symbol', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('funding_rate_coundown_every', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='future_cryptos_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('crypto_historical_pnl',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('crypto_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('avg_entry_price', sa.NUMERIC(), autoincrement=False, nullable=False),
    sa.Column('avg_close_price', sa.NUMERIC(), autoincrement=False, nullable=False),
    sa.Column('percentage_earning', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['crypto_id'], ['future_cryptos.id'], name='crypto_historical_pnl_crypto_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='crypto_historical_pnl_pkey')
    )
    op.drop_table('spot_history')
    op.drop_table('futures_history')
    # ### end Alembic commands ###