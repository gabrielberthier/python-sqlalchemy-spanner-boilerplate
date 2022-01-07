"""create prices table

Revision ID: c9fab842379c
Revises: 83237b012e14
Create Date: 2021-12-28 17:39:39.317623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c9fab842379c"
down_revision = "83237b012e14"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "price",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("sku", sa.BIGINT(), nullable=True),
        sa.Column("unit_price", sa.Float(), nullable=True),
        sa.Column("price_list", sa.String(length=150), nullable=True),
        sa.Column("context", sa.BIGINT(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("price")
