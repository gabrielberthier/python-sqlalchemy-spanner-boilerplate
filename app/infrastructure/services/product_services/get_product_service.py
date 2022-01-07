from fastapi.exceptions import HTTPException
from app.domain.entities.product.product import Product, ProductDto
from app.domain.repositories.product.product_getter_repository import (
    ProductGetterRepository,
)
from app.domain.schemas.product.product_schema import ProductSchema
from app.domain.use_cases.product_cases.add_product_use_case import AddProductUseCase
from app.domain.use_cases.product_cases.get_product_by_sku import GetProductBySku


class GetProductService(GetProductBySku):
    def __init__(self, repository: ProductGetterRepository) -> None:
        self.repository = repository

    def get_product_by_sku(self, sku: int, shallow=False) -> Product:
        product = self.repository.get_product(sku, shallow)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
