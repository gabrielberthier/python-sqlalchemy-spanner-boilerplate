from typing import List
from app.domain.entities.product.product import Product
from app.domain.repositories.product.product_listing_repository import (
    ProductListingRepository,
)
from app.domain.use_cases.product_cases.get_all_products_use_case import (
    GetAllProductsUseCase,
)
from app.domain.use_cases.product_cases.get_product_by_sku import GetProductBySku


class GetAllProductsService(GetAllProductsUseCase):
    def __init__(self, repository: ProductListingRepository) -> None:
        self.repository = repository

    def get_all_products(self, shallow: bool = False) -> List[Product]:
        return self.repository.get_all(shallow)
