from abc import ABC, abstractmethod
from app.domain.entities.product.product import Product
from app.domain.schemas.product.product_schema import ProductSchema


class AddProductUseCase(ABC):
    @abstractmethod
    def add_product(self, command: ProductSchema) -> Product:
        pass
