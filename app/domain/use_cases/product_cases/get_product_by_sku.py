from abc import ABC, abstractmethod
from app.domain.entities.product.product import Product


class GetProductBySku(ABC):
    @abstractmethod
    def get_product_by_sku(self, sku: int) -> Product:
        pass
