from abc import ABC, abstractmethod
from app.domain.entities.product.product import Product, ProductDto


class ProductInserterRepository(ABC):
    @abstractmethod
    def create_product(self, product: ProductDto) -> Product:
        pass
