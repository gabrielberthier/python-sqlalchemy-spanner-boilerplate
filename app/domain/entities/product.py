from pydantic import BaseModel
from typing import List
from app.domain.entities.nutrition import NutritionIdDto
from app.domain.entities.allergen import Allergen
from app.domain.entities.flavour import FlavourIdDto


class ProductSku(BaseModel):
    sku: int
    

class ProductDto(BaseModel):
    sku: int
    name: str
    description: str
    image: str
    combo: int
    

class Product(BaseModel):
    id: int
    sku: int
    name: str
    description: str
    image: str
    combo: int
    nutritions: List[NutritionIdDto] = []
    allergens: Allergen
    ingredients: List[int] = []
    flavour: List[FlavourIdDto] = []
    
    class Config:
        allow_mutation = False


class ProductUpdateDto(BaseModel):
    name: str
    description: str
    image: str
    combo: int
    
    class Config:
        allow_mutation = False
