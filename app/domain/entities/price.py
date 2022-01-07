from pydantic import BaseModel


class PriceDto(BaseModel):
    id: int
    sku: int
    unit_price: float
    price_list: str
    context: int


class Price(BaseModel):
    id: int
    sku: int
    unit_price: float
    price_list: str
    context: int

    class Config:
        allow_mutation = False
