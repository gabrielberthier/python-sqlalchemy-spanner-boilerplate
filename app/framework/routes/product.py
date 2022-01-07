from typing import List
from fastapi import APIRouter, Depends
from app.domain.entities.product.product import Product
from app.domain.schemas.product.product_schema import ProductSchema
from app.domain.use_cases.product_cases.add_product_use_case import AddProductUseCase
from app.domain.use_cases.product_cases.get_all_products_use_case import (
    GetAllProductsUseCase,
)
from app.domain.use_cases.product_cases.get_product_by_sku import GetProductBySku
from app.framework.factories.product_factories.product_services_factories import (
    product_finder_factory,
    product_inserter_factory,
    product_listing_factory,
)


router = APIRouter()


@router.post("/product", response_model=Product)
async def post_product(
    product: ProductSchema,
    service: AddProductUseCase = Depends(product_inserter_factory),
):

    return service.add_product(product)


@router.get("/product/{sku}", response_model=Product)
async def get_product(
    sku: int, service: GetProductBySku = Depends(product_finder_factory)
):

    return service.get_product_by_sku(sku)


@router.get("/product", response_model=List[Product])
async def get_product(
    service: GetAllProductsUseCase = Depends(product_listing_factory),
):
    return service.get_all_products()


# @router.put("/product", response_model=Product)
# async def update_product(
#     sku: int,
#     product: ProductUpdateSchema,
#     service: UpdateProduct = Depends(product_updater_factory),
# ):

#     return service.update_product(sku, product)
