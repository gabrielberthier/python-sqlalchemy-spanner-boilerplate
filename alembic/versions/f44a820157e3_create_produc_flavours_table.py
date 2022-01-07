"""create produc_flavours table

Revision ID: f44a820157e3
Revises: 356727f828f7
Create Date: 2021-12-28 17:58:58.755976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f44a820157e3"
down_revision = "356727f828f7"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product_flavours",
        sa.Column("flavour_id", sa.BIGINT(), nullable=False),
        sa.Column("product_id", sa.BIGINT(), nullable=False),
        sa.ForeignKeyConstraint(
            ["flavour_id"],
            ["flavour.id"],
            name="FK_product_flavours_flavour_FAD4FB45BB18DCF4_1",
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
            name="FK_product_flavours_product_EE8832C55E496E3F_1",
        ),
        sa.PrimaryKeyConstraint("flavour_id", "product_id"),
    )
    op.create_index(
        "IDX_product_flavours_product_id_7BC6C884CC66A759",
        "product_flavours",
        ["product_id"],
        unique=False,
    )


def downgrade():
    op.drop_index(
        "IDX_product_flavours_product_id_7BC6C884CC66A759",
        table_name="product_flavours",
    )
    op.drop_table("product_flavours")
