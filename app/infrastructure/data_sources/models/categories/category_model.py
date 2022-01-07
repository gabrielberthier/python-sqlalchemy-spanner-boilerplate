from uuid import uuid4
from sqlalchemy.sql.sqltypes import Text, String, Integer
from app.infrastructure.database.db import Base
from sqlalchemy.sql.schema import Column, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import relationship
from .product_categories import product_categories


class CategoryModel(Base):
    __tablename__ = "category"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )
    plk_id = Column("plk_id", Integer)
    name = Column(String, nullable=False)
    products = relationship(
        "ProductModel", secondary=product_categories, backref="categories"
    )

    image_url = Column(Text)
    display_order = Column(Integer)
    color = Column(String)
    parent_category = Column(Integer)


Index("uix_plk_id", CategoryModel.plk_id, unique=True)
