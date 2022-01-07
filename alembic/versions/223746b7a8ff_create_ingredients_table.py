"""create ingredients table

Revision ID: 223746b7a8ff
Revises: 
Create Date: 2021-12-28 17:36:09.027881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "223746b7a8ff"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "ingredient",
        sa.Column("uuid", sa.String(), primary_key=True),
        sa.Column("id", sa.BIGINT(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=True),
        sa.Column("measure_unity", sa.String(length=255), nullable=True),
        sa.Column("min_value", sa.NUMERIC(precision=38, scale=9), nullable=True),
        sa.Column("max_value", sa.NUMERIC(precision=38, scale=9), nullable=True),
    )


def downgrade():
    op.drop_table("ingredient")
