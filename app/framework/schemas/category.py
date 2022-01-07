from pydantic import BaseModel
from typing import List, Optional


class CategoryIdSchema(BaseModel):
    id: int


class CategorySchema(CategoryIdSchema):
    name: str
    image_url: str
    display_order: int
    color: str
    parent_category: Optional[int]
    skus: List[int] = []

    class Config:
        orm_mode = True


class CategoryUpdateSchema(CategoryIdSchema):
    name: str
    image_url: str
    display_order: int
    color: str
    parent_category: Optional[int]

    class Config:
        orm_mode = True
