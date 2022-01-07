from typing import List
from pydantic.main import BaseModel


class Ingredient(BaseModel):
    id: int
    name: str
    unit_measure: str
    min_value: float
    max_value: float

    class Config:
        allow_mutation = False


class IngredientList(BaseModel):
    ingredient_list: List[Ingredient] = []

    class Config:
        allow_mutation = False


class UpdateIngredientSchema(BaseModel):
    name: str
    unit_measure: str
    min_value: float
    max_value: float

    class Config:
        allow_mutation = False
