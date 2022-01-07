from abc import ABC, abstractmethod
from app.domain.entities.product.product import Product, ProductDto


class ProductGetterRepository(ABC):
    @abstractmethod
    def get_product(self, sku: int, shallow=False) -> Product:
        pass
