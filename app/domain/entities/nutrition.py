from pydantic import BaseModel


class NutritionDto(BaseModel):
    description: str
    

class NutritionIdDto(BaseModel):
    id: int
    

class Nutrition(BaseModel):
    id: int
    description: str
    
    class Config:
        allow_mutation = False
