from typing import Optional
from pydantic import BaseModel
from decimal import Decimal


class ProductIngredient(BaseModel):
    id: int
    measure_unity: Optional[str]
    min_value: Optional[Decimal]
    max_value: Optional[Decimal]
    description: Optional[str]
