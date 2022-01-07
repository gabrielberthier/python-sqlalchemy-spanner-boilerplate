"""create ingredient_presence table

Revision ID: 356727f828f7
Revises: 90ea6f777cec
Create Date: 2021-12-28 17:57:26.458214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "356727f828f7"
down_revision = "90ea6f777cec"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "ingredient_presence",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("ingredient_id", sa.BIGINT(), nullable=True),
        sa.Column("product_id", sa.BIGINT(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("last_updated", sa.TIMESTAMP(), nullable=True),
        sa.ForeignKeyConstraint(
            ["ingredient_id"],
            ["ingredient.id"],
            name="FK_ingredient_presence_ingredient_74AEF14B905CBA5B_1",
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
            name="FK_ingredient_presence_product_E40C9971FB5A1120_1",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "IDX_ingredient_presence_product_id_N_4E3D3711CCBB8133",
        "ingredient_presence",
        ["product_id"],
        unique=False,
    )
    op.create_index(
        "IDX_ingredient_presence_ingredient_id_N_A3C09FED0B075789",
        "ingredient_presence",
        ["ingredient_id"],
        unique=False,
    )


def downgrade():
    op.drop_index(
        "IDX_ingredient_presence_ingredient_id_N_A3C09FED0B075789",
        table_name="ingredient_presence",
    )
    op.drop_index(
        "IDX_ingredient_presence_product_id_N_4E3D3711CCBB8133",
        table_name="ingredient_presence",
    )
    op.drop_table("ingredient_presence")
