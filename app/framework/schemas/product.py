from pydantic import BaseModel
from typing import List
from app.framework.schemas.flavour import FlavourIdSchema
from app.framework.schemas.nutrition import NutritionIdSchema
from app.framework.schemas.allergen import AllergenSchema


class ProductIdSchema(BaseModel):
    id: int
    
    
class ProductSkuSchema(BaseModel):
    sku: int
       
  
class ProductSchema(ProductIdSchema):
    sku: int
    name: str
    description: str
    image: str
    combo: int
    nutrition: List[NutritionIdSchema] = []
    allergens: AllergenSchema
    ingredients: List[int] = []
    flavour: List[FlavourIdSchema] = []
    
    class Config:
        orm_mode = True
        

class ProductUpdateSchema(BaseModel):
    name: str
    description: str
    image: str
    combo: int
    
    class Config:
        orm_model = True
