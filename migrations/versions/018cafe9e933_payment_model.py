"""payment model

Revision ID: 018cafe9e933
Revises: 31a64fecd30d
Create Date: 2022-10-19 21:32:59.018469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '018cafe9e933'
down_revision = '31a64fecd30d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoice',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('merchant_request_id', sa.String(), nullable=False),
    sa.Column('paymentType', sa.String(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('receipt_id', sa.String(length=100), nullable=False),
    sa.Column('date_paid', sa.DateTime(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('merchant_request_id', sa.String(length=100), nullable=True),
    sa.Column('phoneNumber', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction')
    op.drop_table('invoice')
    # ### end Alembic commands ###
