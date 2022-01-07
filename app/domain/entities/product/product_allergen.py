from typing import Optional
from pydantic import BaseModel
from app.domain.entities.allergens.allergen_type import AllergenType


class ProductAllergen(BaseModel):
    id: int
    description: str
    may_have: bool
    contain: bool
    type: AllergenType


class ProductAllergenDto(BaseModel):
    id: int
    may_have: bool = False
    contain: bool = False
    description: Optional[str]
