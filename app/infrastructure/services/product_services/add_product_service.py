from fastapi.exceptions import HTTPException
from app.domain.entities.product.product import Product, ProductDto
from app.domain.repositories.product.product_inserter_repository import (
    ProductInserterRepository,
)
from app.domain.schemas.product.product_schema import ProductSchema
from app.domain.use_cases.product_cases.add_product_use_case import AddProductUseCase
from app.domain.use_cases.product_cases.get_product_by_sku import GetProductBySku
from app.infrastructure.data_sources.adapter_repositories.product.product_alchemy_repository import (
    AlreadyRegisteredProductException,
)


class AddProductService(AddProductUseCase):
    def __init__(self, repository: ProductInserterRepository) -> None:
        self.repository = repository

    def construct_insertion_dto(self, command: ProductSchema) -> ProductDto:
        allergens = command.allergens.to_entity() if command.allergens else []
        ingredients = command.ingredients
        flavours = [c.to_entity() for c in command.flavour]
        nutrition = [c.to_entity() for c in command.nutrition]

        values = {
            **command.dict(),
            "allergens": allergens,
            "nutrition": nutrition,
            "flavours": flavours,
            "ingredients": ingredients,
        }

        return ProductDto(**values)

    def add_product(self, command: ProductSchema) -> Product:
        try:
            return self.repository.create_product(self.construct_insertion_dto(command))
        except AlreadyRegisteredProductException:
            raise HTTPException(status_code=400, detail="Product already registered")

    # def get_product_by_sku(self, sku: int) -> Product:
    #     product = self.repository.get_product(sku)
    #     if not product:
    #         raise HTTPException(status_code=404, detail="Product not found")
    #     return product

    # def update_product(self, sku: int, command: ProductUpdateSchema) -> Product:
    #     product = self.repository.update_product(sku, command)
    #     if not product:
    #         raise HTTPException(status_code=404, detail="Product not found")
    #     return product
