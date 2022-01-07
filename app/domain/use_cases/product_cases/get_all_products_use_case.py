from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.product.product import Product


class GetAllProductsUseCase(ABC):
    @abstractmethod
    def get_all_products(self, shallow: bool = False) -> List[Product]:
        pass
