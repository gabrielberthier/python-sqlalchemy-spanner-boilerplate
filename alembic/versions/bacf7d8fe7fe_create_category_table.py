"""create category table

Revision ID: bacf7d8fe7fe
Revises: ae7b8f8599c9
Create Date: 2021-12-28 17:47:59.035794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bacf7d8fe7fe"
down_revision = "ae7b8f8599c9"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "category",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("name", sa.String(length=250), nullable=False),
        sa.Column("image_url", sa.String(length=500), nullable=True),
        sa.Column("display_order", sa.BIGINT(), nullable=True),
        sa.Column("color", sa.String(length=200), nullable=True),
        sa.Column("parent_category", sa.BIGINT(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("category")
