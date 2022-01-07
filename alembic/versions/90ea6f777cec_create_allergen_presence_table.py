"""create allergen_presence table

Revision ID: 90ea6f777cec
Revises: 295a96ca7a6f
Create Date: 2021-12-28 17:56:34.425942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "90ea6f777cec"
down_revision = "295a96ca7a6f"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "allergen_presence",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("allergen_id", sa.BIGINT(), nullable=True),
        sa.Column("product_id", sa.BIGINT(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("last_updated", sa.TIMESTAMP(), nullable=True),
        sa.Column("description", sa.String(length=455), nullable=True),
        sa.Column("may_have", sa.Boolean(), nullable=True),
        sa.Column("contain", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(
            ["allergen_id"],
            ["allergen.id"],
            name="FK_allergen_presence_allergen_C64D91B929E3B781_1",
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
            name="FK_allergen_presence_product_630F6F2B10C00EF8_1",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "IDX_allergen_presence_product_id_N_666E944331CA16C3",
        "allergen_presence",
        ["product_id"],
        unique=False,
    )
    op.create_index(
        "IDX_allergen_presence_allergen_id_N_A08A81E487DD8D1E",
        "allergen_presence",
        ["allergen_id"],
        unique=False,
    )


def downgrade():
    op.drop_index(
        "IDX_allergen_presence_allergen_id_N_A08A81E487DD8D1E",
        table_name="allergen_presence",
    )
    op.drop_index(
        "IDX_allergen_presence_product_id_N_666E944331CA16C3",
        table_name="allergen_presence",
    )
    op.drop_table("allergen_presence")
