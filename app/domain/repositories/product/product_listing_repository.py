from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.product.product import Product, ProductDto


class ProductListingRepository(ABC):
    @abstractmethod
    def get_all(self, shallow=False) -> List[Product]:
        pass
