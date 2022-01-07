from pydantic import BaseModel
from typing import List, Optional

from app.domain.entities.product.product import Product


class CategoryDto(BaseModel):
    id: int
    name: str
    image_url: str
    display_order: int
    color: str
    parent_category: Optional[int]
    skus: List[int] = []

    class Config:
        allow_mutation = False


class Category(BaseModel):
    id: str
    plk_id: int
    name: str
    image_url: str
    display_order: int
    color: str
    parent_category: Optional[int]
    products: List[Product] = []

    class Config:
        allow_mutation = False


class CategoryUpdateDto(BaseModel):
    name: str
    image_url: str
    display_order: int
    color: str
    parent_category: Optional[int]

    class Config:
        allow_mutation = False
