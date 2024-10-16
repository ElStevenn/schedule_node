"""Sync with new database

Revision ID: 0f19aa5bcf7f
Revises: 2db02544daae
Create Date: 2024-09-19 11:57:54.736355

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f19aa5bcf7f'
down_revision: Union[str, None] = '2db02544daae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('surname', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('url_picture', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('accounts',
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('google_oauth',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('access_token', sa.Text(), nullable=True),
    sa.Column('refresh_token', sa.Text(), nullable=True),
    sa.Column('expires_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('monthly_subscription',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('subscription_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_configuration',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('minimum_founding_rate_to_show', sa.Float(), nullable=True),
    sa.Column('columns_to_show', sa.Text(), nullable=True),
    sa.Column('main_used_exchange', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historical_pnl',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('avg_entry_price', sa.String(length=255), nullable=True),
    sa.Column('side', sa.String(length=10), nullable=False),
    sa.Column('pnl', sa.Float(), nullable=False),
    sa.Column('net_profits', sa.Float(), nullable=False),
    sa.Column('opening_fee', sa.Float(), nullable=True),
    sa.Column('closing_fee', sa.Float(), nullable=True),
    sa.Column('closed_value', sa.Float(), nullable=False),
    sa.Column('account_id', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('historical_pnl')
    op.drop_table('user_configuration')
    op.drop_table('monthly_subscription')
    op.drop_table('google_oauth')
    op.drop_table('accounts')
    op.drop_table('users')
    # ### end Alembic commands ###
