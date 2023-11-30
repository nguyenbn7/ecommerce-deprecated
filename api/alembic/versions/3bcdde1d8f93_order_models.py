"""order models

Revision ID: 3bcdde1d8f93
Revises: 4899a7d9d376
Create Date: 2023-11-30 17:18:41.058754

"""
import json
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3bcdde1d8f93'
down_revision: Union[str, None] = '4899a7d9d376'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('billing_addresses',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('address2', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('zip_code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    delivery_methods_tbl = op.create_table('delivery_methods',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('short_name', sa.String(), nullable=False),
    sa.Column('delivery_time', sa.String(), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_methods',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shipping_addresses',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('address2', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('state', sa.String(), nullable=False),
    sa.Column('zip_code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('status', sa.Enum('PENDING', 'PAYMENT_RECEIVED', 'PAYMENT_FAILED', name='orderstatus'), nullable=False),
    sa.Column('payment_method', sa.String(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('delivery_method_id', sa.BigInteger(), nullable=False),
    sa.Column('billing_address_id', sa.BigInteger(), nullable=False),
    sa.Column('shipping_address_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['billing_address_id'], ['billing_addresses.id'], ),
    sa.ForeignKeyConstraint(['delivery_method_id'], ['delivery_methods.id'], ),
    sa.ForeignKeyConstraint(['shipping_address_id'], ['shipping_addresses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_items',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('picture_url', sa.String(), nullable=False),
    sa.Column('brand', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('order_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

    with open("alembic/data/delivery.json") as json_file:
        json_data = json.load(json_file)
        op.bulk_insert(delivery_methods_tbl, json_data)


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_table('orders')
    op.drop_table('shipping_addresses')
    op.drop_table('payment_methods')
    op.drop_table('delivery_methods')
    op.drop_table('billing_addresses')
    # ### end Alembic commands ###
