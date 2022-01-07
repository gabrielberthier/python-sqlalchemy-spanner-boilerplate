from typing import Optional
from pydantic import BaseModel
from app.domain.entities.nutrition.nutrition_type import NutritionType
from decimal import Decimal


class Nutrition(BaseModel):
    id: int
    nutrition_type: NutritionType
    value: Decimal


class NutritionDto(BaseModel):
    id: Optional[int]
    description: str
