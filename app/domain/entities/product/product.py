from __future__ import annotations
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from decimal import Decimal
from app.domain.entities.nutrition.nutrition import Nutrition
from app.domain.entities.flavour.flavour import Flavour
from app.domain.entities.ingredients.ingredient import Ingredient
from datetime import datetime

from app.domain.entities.product.product_allergen import (
    ProductAllergen,
    ProductAllergenDto,
)
from app.domain.entities.product.product_nutrition import ProductNutrition


class Product(BaseModel):
    # Código do produto no PLKOffice/Aqui
    id: str
    # Código do produto no PLKOffice
    plk_id: int
    # Código do produto no SAP
    sku: int
    # Data da última modificação
    modified_at: datetime = Field(datetime.now(), alias="updated_at")
    # Nome digital do produto
    name: str
    # Descrição do produto
    description: str
    # Caminho da imagem
    image: str
    # SKU do set/combo
    combo: Optional[int]
    # Alergênicos do produto
    allergens: List[ProductAllergen] = []
    # Ingredientes do produto
    ingredients: List[Ingredient] = []
    # Sabores do produto
    flavours: List[Flavour] = []
    # Nutrientes
    nutrition: List[Nutrition] = []


class ProductDto(BaseModel):
    # Código do produto no PLKOffice
    id: Optional[int]
    # Código do produto no SAP
    sku: int
    # Data da última modificação
    modified_at: datetime = Field(datetime.now(), alias="updated_at")
    # Nome digital do produto
    name: str
    # Descrição do produto
    description: str
    # Caminho da imagem
    image: str
    # SKU do set/combo
    combo: Optional[int]
    # Alergênicos do produto
    allergens: List[ProductAllergenDto] = []
    # Ingredientes do produto
    ingredients: List[int] = []
    # Sabores do produto
    flavours: List[Flavour] = []
    # Nutrientes
    nutrition: List[ProductNutrition] = []

    def base_as_dict(self):
        return {
            "plk_id": self.id,
            "sku": self.sku,
            "modified_at": self.modified_at,
            "name": self.name,
            "description": self.description,
            "image": self.image,
            "combo": self.combo,
        }
