from datetime import datetime
from app.domain.entities.ingredients.ingredient import Ingredient
from app.domain.entities.product.product import Product
from app.domain.repositories.ingredients.ingredients_repository import (
    IngredientsRepository,
)
from unittest import main, TestCase, mock
from app.domain.repositories.product.product_inserter_repository import (
    ProductInserterRepository,
)
from app.domain.schemas.product.product_schema import ProductSchema

from app.domain.use_cases.product_cases.add_product_use_case import AddProductUseCase
from app.infrastructure.data_sources.adapter_repositories.product.product_alchemy_repository import (
    AlreadyRegisteredProductException,
)
from app.infrastructure.services.product_services.add_product_service import (
    AddProductService,
)
from fastapi.exceptions import HTTPException


def create_stub_product():
    values = {
        "id": 2,
        "sku": 2,
        "modified_at": datetime.now(),
        "name": "Product",
        "description": "Description",
        "image": "str/path",
        "combo": None,
    }
    return Product(**values)


def create_stub_schema():
    values = {**create_stub_product().dict(), "event": "", "allergens": None}

    return ProductSchema(**values)


class TestAddProductUseCase(TestCase):
    def setUp(self) -> None:
        self.repository = mock.MagicMock(autospec=ProductInserterRepository)
        self.sut: AddProductUseCase = AddProductService(self.repository)

    def test_should_return_400_with_taken_sku(self):
        with self.assertRaises(HTTPException) as context:
            repository = mock.Mock()
            repository.create_product.side_effect = AlreadyRegisteredProductException()
            values = {
                **create_stub_product().dict(),
                "event": "",
                "allergens": None,
            }
            sut: AddProductUseCase = AddProductService(repository)
            response = sut.add_product(ProductSchema(**values))

        self.assertIsNotNone(context)

        self.assertEquals(context.exception.status_code, 400)

    def test_should_fail_if_repository_fails(self):
        repository = mock.MagicMock(autospec=ProductInserterRepository)
        repository.create_product.side_effect = Exception()
        with self.assertRaises(Exception) as context:
            sut: AddProductUseCase = AddProductService(repository)
            sut.add_product(create_stub_schema())

        print(context.exception)

    def test_should_call_repository(self):
        with mock.patch(
            "app.infrastructure.services.product_services.add_product_service.ProductInserterRepository"
        ) as MockedRepository:
            mc: mock.Mock = MockedRepository.return_value

            sut: AddProductUseCase = AddProductService(mc)
            sut.add_product(create_stub_schema())

            mc.create_product.assert_called_once()

    def test_should_insert_raw_product(self):
        with mock.patch(
            "app.infrastructure.services.product_services.add_product_service.ProductInserterRepository"
        ) as MockedRepository:
            mc: mock.Mock = MockedRepository.return_value

            schema = create_stub_schema()
            mc.create_product.return_value = Product(
                **{**schema.dict(), "allergens": []}
            )
            sut: AddProductUseCase = AddProductService(mc)
            response = sut.add_product(schema)

            mc.create_product.assert_called_once()
            response.id = 2
            response.name = "Product"


if __name__ == "__main__":
    main()
