from datetime import datetime
from typing import List
from sqlalchemy import Integer, String, Column, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Index, UniqueConstraint
from app.infrastructure.database.db import Base
from uuid import uuid4


class ProductModel(Base):
    __tablename__ = "product"
    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    # Código do produto no PLKOffice
    plk_id = Column(Integer)
    # Modificação na origem (provavelmente PLKOffice)
    modified_at = Column(DateTime)
    # Código do produto no SAP
    sku = Column(Integer)
    # Nome digital do produto
    name = Column(String)
    # Descrição do produto
    description = Column(String)
    # Caminho da imagem
    image = Column(Text)
    # SKU do set/combo
    combo = Column(Integer, nullable=True)
    # Ultima atualização
    updated_at = Column(
        "last_updated", DateTime, default=datetime.now, onupdate=datetime.now
    )

    allergens: List = relationship("AllergenPresence", back_populates="product")
    ingredients: List = relationship("IngredientPresence", back_populates="product")


Index("uix_plk_id", ProductModel.plk_id, unique=True)
Index("uix_sku_id", ProductModel.sku, unique=True)
