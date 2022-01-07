from app.domain.entities.product.product import Product
from app.infrastructure.data_sources.models.products.product_model import ProductModel


class ProductAdapter:
    def make_product(self, model: ProductModel) -> Product:
        return Product(**model.__dict__)
