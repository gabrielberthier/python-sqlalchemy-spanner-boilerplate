from pydantic import BaseModel


class NutritionType(BaseModel):
    type: str
    description: str
