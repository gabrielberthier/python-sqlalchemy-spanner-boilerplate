from pydantic import BaseModel


class AllergenDto(BaseModel):
    id: int
    description: str
    type: int


class Allergen(BaseModel):
    id: int
    description: str
    type: int

    class Config:
        allow_mutation = False
