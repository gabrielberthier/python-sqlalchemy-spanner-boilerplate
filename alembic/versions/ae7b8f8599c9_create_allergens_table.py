"""create allergens table

Revision ID: ae7b8f8599c9
Revises: 65d2793c86d4
Create Date: 2021-12-28 17:47:26.133764

"""
from alembic import op
import sqlalchemy as sa
from app.infrastructure.data_sources.models.allergens.allergen_model import (
    AllergenModel,
)

# revision identifiers, used by Alembic.
revision = "ae7b8f8599c9"
down_revision = "65d2793c86d4"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "allergen",
        sa.Column("id", sa.BIGINT(), nullable=False),
        sa.Column("type", sa.String(length=255), nullable=True),
        sa.Column("description", sa.String(length=300), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.bulk_insert(
        AllergenModel.__table__,
        [
            [
                {"id": 1, "description": "GLÚTEN", "type": 2},
                {"id": 2, "description": "LACTOSE", "type": 2},
                {"id": 3, "description": "OVO", "type": 1},
                {"id": 4, "description": "DERIVADOS DE OVO", "type": 1},
                {"id": 5, "description": "TRIGO", "type": 1},
                {"id": 6, "description": "DERIVADOS DE TRIGO", "type": 1},
                {"id": 7, "description": "FARINHA", "type": 1},
                {"id": 8, "description": "SOJA", "type": 1},
                {"id": 9, "description": "DERIVADOS DE SOJA", "type": 1},
                {"id": 10, "description": "TRAÇOS DE SOJA", "type": 1},
                {"id": 11, "description": "LETICINA DE SOJA", "type": 1},
                {"id": 12, "description": "CENTEIO", "type": 1},
                {"id": 13, "description": "CEVADA", "type": 1},
                {"id": 14, "description": "AVEIA", "type": 1},
                {"id": 15, "description": "DERIVADOS DE AVEIA", "type": 1},
                {"id": 16, "description": "LEITE", "type": 1},
                {"id": 17, "description": "LEITE DE VACA", "type": 1},
                {"id": 18, "description": "DERIVADOS DE LEITE", "type": 1},
                {"id": 19, "description": "GLUTAMATO MONOSSÓDICO", "type": 1},
                {"id": 20, "description": "SULFITO", "type": 1},
                {"id": 21, "description": "NOZES", "type": 1},
                {"id": 22, "description": "NOZ PEÇÃ", "type": 1},
                {"id": 23, "description": "PEIXE", "type": 1},
                {"id": 24, "description": "DERIVADO DE PEIXES", "type": 1},
                {
                    "id": 25,
                    "description": "CRUSTÁCEOS (MACROBRACHIUM E/OU PENAEUS)",
                    "type": 1,
                },
                {
                    "id": 26,
                    "description": "DERIVADOS DE CRUSTÁCEOS (MACROBRACHIUM E/OU PENAEUS)",
                    "type": 1,
                },
                {"id": 27, "description": "AMIDO DE MILHO TRANSGÊNICO", "type": 1},
                {"id": 28, "description": "AMENDOIM", "type": 1},
                {"id": 29, "description": "AMÊNDOA", "type": 1},
                {"id": 30, "description": "AVELÃ", "type": 1},
                {"id": 31, "description": "CASTANHAS", "type": 1},
                {"id": 32, "description": "CASTANHA-DE-CAJU", "type": 1},
                {"id": 33, "description": "CASTANHA-DO-PARÁ", "type": 1},
                {"id": 34, "description": "MALTE", "type": 1},
                {"id": 35, "description": "CASTANHA DO BRASIL", "type": 1},
                {"id": 36, "description": "CEVADA AVELÃ", "type": 1},
                {"id": 37, "description": "LÁTEX NATURAL", "type": 1},
                {"id": 38, "description": "AROMATIZANTE", "type": 1},
                {
                    "id": 39,
                    "description": "AROMATIZANTE IDÊNTICO AO NATURAL",
                    "type": 1,
                },
                {
                    "id": 40,
                    "description": "AROMATIZANTE SINTÉTICO IDÊNTICO AO NATURAL",
                    "type": 1,
                },
                {"id": 41, "description": "FENILALANINA", "type": 1},
                {"id": 42, "description": "MOSTARDA e MACADÂMIA", "type": 1},
            ]
        ],
    )


def downgrade():
    op.drop_table("allergen")
