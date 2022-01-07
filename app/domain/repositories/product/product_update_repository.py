from abc import ABC, abstractmethod
from app.domain.entities.product.product import Product, ProductDto


class ProductUpdateRepository(ABC):
    @abstractmethod
    def update_product(self, sku: int) -> Product:
        pass
