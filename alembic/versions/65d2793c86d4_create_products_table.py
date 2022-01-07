"""create products table

Revision ID: 65d2793c86d4
Revises: c9fab842379c
Create Date: 2021-12-28 17:41:02.182212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "65d2793c86d4"
down_revision = "c9fab842379c"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("modified_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("sku", sa.BIGINT(), nullable=True),
        sa.Column("name", sa.String(length=350), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("image", sa.String(length=350), nullable=True),
        sa.Column("combo", sa.BIGINT(), nullable=True),
        sa.Column("last_updated", sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("product")
