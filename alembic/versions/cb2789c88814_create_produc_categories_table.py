"""create produc_categories table

Revision ID: cb2789c88814
Revises: f44a820157e3
Create Date: 2021-12-28 18:00:44.329854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "cb2789c88814"
down_revision = "f44a820157e3"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product_categories",
        sa.Column("category_id", sa.BIGINT(), nullable=False),
        sa.Column("product_id", sa.BIGINT(), nullable=False),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["category.id"],
            name="FK_product_categories_category_6E16600EC9776B6E_1",
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
            name="FK_product_categories_product_40B7CA2512B05F5D_1",
        ),
        sa.PrimaryKeyConstraint("category_id", "product_id"),
    )
    op.create_index(
        "IDX_product_categories_product_id_93D59B85C6167F28",
        "product_categories",
        ["product_id"],
        unique=False,
    )


def downgrade():
    op.drop_index(
        "IDX_product_categories_product_id_93D59B85C6167F28",
        table_name="product_categories",
    )
    op.drop_table("product_categories")
