"""create nutrition_info table

Revision ID: 4b3d29a3d018
Revises: cb2789c88814
Create Date: 2021-12-28 18:01:34.693883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4b3d29a3d018"
down_revision = "cb2789c88814"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "nutrition_info",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("nutrition_id", sa.BIGINT(), nullable=True),
        sa.Column("product_id", sa.BIGINT(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("last_updated", sa.TIMESTAMP(), nullable=True),
        sa.Column("value", sa.NUMERIC(precision=38, scale=9), nullable=True),
        sa.ForeignKeyConstraint(
            ["nutrition_id"],
            ["nutrition.id"],
            name="FK_nutrition_info_nutrition_6EF3A7BA9E70E1D7_1",
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
            name="FK_nutrition_info_product_544E4F34B97A798C_1",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "IDX_nutrition_info_product_id_N_C77218ED7CFDC8A2",
        "nutrition_info",
        ["product_id"],
        unique=False,
    )
    op.create_index(
        "IDX_nutrition_info_nutrition_id_N_E9CC34A1CC9CE091",
        "nutrition_info",
        ["nutrition_id"],
        unique=False,
    )


def downgrade():
    op.drop_index(
        "IDX_nutrition_info_nutrition_id_N_E9CC34A1CC9CE091",
        table_name="nutrition_info",
    )
    op.drop_index(
        "IDX_nutrition_info_product_id_N_C77218ED7CFDC8A2", table_name="nutrition_info"
    )
    op.drop_table("nutrition_info")
