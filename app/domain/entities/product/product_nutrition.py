from pydantic import BaseModel
from decimal import Decimal


class ProductNutrition(BaseModel):
    key: int
    value: Decimal
