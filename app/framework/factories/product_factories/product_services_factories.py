from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.domain.use_cases.product_cases.add_product_use_case import AddProductUseCase
from app.domain.use_cases.product_cases.get_all_products_use_case import (
    GetAllProductsUseCase,
)
from app.domain.use_cases.product_cases.get_product_by_sku import GetProductBySku
from app.infrastructure.data_sources.adapter_repositories.product.product_alchemy_repository import (
    ProductAlchemyRepository,
)
from app.infrastructure.database.db import get_db
from app.infrastructure.services.product_services.add_product_service import (
    AddProductService,
)
from app.infrastructure.services.product_services.get_all_products_service import (
    GetAllProductsService,
)
from app.infrastructure.services.product_services.get_product_service import (
    GetProductService,
)


def product_inserter_factory(db: Session = Depends(get_db)) -> AddProductUseCase:
    service: AddProductUseCase = AddProductService(ProductAlchemyRepository(db))
    return service


def product_finder_factory(db: Session = Depends(get_db)) -> GetProductBySku:
    service: GetProductBySku = GetProductService(ProductAlchemyRepository(db))
    return service


def product_listing_factory(db: Session = Depends(get_db)) -> GetAllProductsUseCase:
    service: GetAllProductsUseCase = GetAllProductsService(ProductAlchemyRepository(db))
    return service


# def product_updater_factory(db: Session = Depends(get_db)) -> UpdateProduct:
#     service: UpdateProduct = ProductService(ProductAlchemyRepository(db))
#     return service
