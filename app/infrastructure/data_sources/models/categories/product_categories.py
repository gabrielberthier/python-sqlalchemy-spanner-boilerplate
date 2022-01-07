from sqlalchemy import Table
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from app.infrastructure.database.db import Base

product_categories = Table(
    "product_categories",
    Base.metadata,
    Column(
        "category_id",
        String(36),
        ForeignKey("category.id"),
        primary_key=True,
    ),
    Column(
        "product_id",
        String(36),
        ForeignKey("product.id"),
        primary_key=True,
    ),
)
