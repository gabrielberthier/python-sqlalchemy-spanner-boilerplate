from pydantic import BaseModel


class Flavour(BaseModel):
    id: int
    description: str
