from pydantic import BaseModel


class AllergenType(BaseModel):
    type: str
    description: str
