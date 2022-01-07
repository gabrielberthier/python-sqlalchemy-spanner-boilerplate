from typing import List, Optional
from pydantic import BaseModel
from decimal import Decimal

# MUST DO: map in the database as ingredient_info and product_ingredient,
# splitting this n:n relationship
class Ingredient(BaseModel):
    id: Optional[int]
    name: str
    measure_unity: Optional[str]
    min_value: Optional[Decimal]
    max_value: Optional[Decimal]

    class Config:
        allow_mutation = False


class IngredientDto(BaseModel):
    id: Optional[int]
    name: str


class IngredientList(BaseModel):
    ingredient_list: List[Ingredient] = []

    class Config:
        allow_mutation = False


class UpdateIngredient(BaseModel):
    name: Optional[str]
    measure_unity: Optional[str]
    min_value: Optional[float]
    max_value: Optional[float]

    class Config:
        allow_mutation = False


class DeleteIngredient(BaseModel):
    id: int

    class Config:
        allow_mutation = False
