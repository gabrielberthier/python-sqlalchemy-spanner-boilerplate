from typing import List
from sqlalchemy.orm.session import Session
from app.domain.entities.product.product import Product, ProductDto
from app.domain.repositories.product.product_getter_repository import (
    ProductGetterRepository,
)
from app.domain.repositories.product.product_inserter_repository import (
    ProductInserterRepository,
)
from app.domain.repositories.product.product_listing_repository import (
    ProductListingRepository,
)
from app.infrastructure.data_sources.adapter_repositories.product.product_adapter import (
    ProductAdapter,
)
from app.infrastructure.data_sources.models.products.product_model import ProductModel
from sqlalchemy.exc import IntegrityError
import traceback


class AlreadyRegisteredProductException(Exception):
    pass


class ProductAlchemyRepository(
    ProductGetterRepository, ProductInserterRepository, ProductListingRepository
):
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_product(self, sku: int, shallow=False) -> Product:
        model = self.db.query(ProductModel).filter(ProductModel.sku == sku).first()

        product_adapter = ProductAdapter()

        product = product_adapter.make_product(model, shallow) if model else None

        self.db.commit()

        return product

    def create_product(self, product: ProductDto) -> Product:
        try:

            product_model = ProductModel(product.base_as_dict())

            self.db.add(product_model)

            self.db.commit()

            self.db.refresh(product_model)

            product_adapter = ProductAdapter()

            product = product_adapter.make_product(product_model)

            self.db.commit()

            return product
        except IntegrityError as ex:
            self.db.rollback()
            print(ex)
            traceback.print_exc()
            raise AlreadyRegisteredProductException
        except Exception as ex:
            print(ex)
            traceback.print_exc()
            self.db.rollback()

    def get_all(self) -> List[Product]:
        product_adapter = ProductAdapter()

        products = [
            product_adapter.make_product(model)
            for model in self.db.query(ProductModel).all()
        ]

        self.db.commit()

        return products

    # def update_product(self, sku: int, product: ProductUpdateDto) -> Product:
    #     model = self.get_product(sku)
    #     if model:
    #         model.name = product.name
    #         model.description = product.description
    #         model.image = product.image
    #         model.combo = product.combo
    #     self.db.commit()
    #     self.db.refresh()
    #     return Product(**model.__dict__)
