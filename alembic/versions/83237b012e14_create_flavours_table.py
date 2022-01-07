"""create flavours table

Revision ID: 83237b012e14
Revises: 223746b7a8ff
Create Date: 2021-12-28 17:37:55.108562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "83237b012e14"
down_revision = "223746b7a8ff"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "flavour",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("description", sa.TEXT(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("flavour")
