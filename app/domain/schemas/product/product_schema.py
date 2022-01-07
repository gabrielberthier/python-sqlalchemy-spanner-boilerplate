from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel


class ProductSchema(BaseModel):
    event: str
    modified_by: Optional[Dict] = None
    modified_at: datetime
    id: int
    sku: int
    name: str
    description: str
    image: Optional[str]
    combo: Optional[int]

    ingredients: List[int] = []

    class Config:
        orm_mode = True
