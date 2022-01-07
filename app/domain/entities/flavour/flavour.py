from pydantic import BaseModel


class FlavourIdDto(BaseModel):
    id: int


class FlavourDto(FlavourIdDto):
    description: str


class Flavour(BaseModel):
    id: int
    description: str

    class Config:
        allow_mutation = False
