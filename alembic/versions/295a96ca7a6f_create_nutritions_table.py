"""create nutritions table

Revision ID: 295a96ca7a6f
Revises: bacf7d8fe7fe
Create Date: 2021-12-28 17:50:06.863666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "295a96ca7a6f"
down_revision = "bacf7d8fe7fe"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "nutrition",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("description", sa.String(length=450), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("nutrition")
