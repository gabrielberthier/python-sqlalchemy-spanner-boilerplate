from typing import List
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str
    image_url: str
    display_order: int
    color: str
    parent_category: int
    # Lista dos ids dos produtos vinculados
    skus: List[int] = []
