from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.infrastructure.database.db import Base


categories_products = Table(
    'categories_product',
    Base.metadata,
    Column('category_id', Integer, ForeignKey('category.id')),
    Column('product_id', Integer, ForeignKey('product.id'))
)


class CategoryModel(Base):
    __tablename__ = 'category'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_url = Column(String)
    display_order = Column(Integer)
    color = Column(String)
    parent_category = Column(Integer)
