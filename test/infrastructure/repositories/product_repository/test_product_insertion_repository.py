from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.functions import random
from app.domain.entities.flavour.flavour import Flavour
from app.domain.entities.ingredients.ingredient import IngredientDto
from app.domain.entities.product.product import ProductDto
from app.domain.entities.product.product_allergen import ProductAllergenDto
from app.domain.entities.product.product_ingredient import ProductIngredient
from app.domain.entities.product.product_nutrition import ProductNutrition
from app.domain.repositories.product.product_inserter_repository import (
    ProductInserterRepository,
)
from app.infrastructure.data_sources.adapter_repositories.product.product_alchemy_repository import (
    AlreadyRegisteredProductException,
    ProductAlchemyRepository,
)
from app.infrastructure.data_sources.models.allergens.allergen_model import (
    AllergenModel,
)
from app.infrastructure.data_sources.models.flavours.flavour_model import FlavourModel
from app.infrastructure.data_sources.models.ingredients.ingredients_model import (
    IngredientModel,
)
from app.infrastructure.data_sources.models.nutrition.nutrition_model import (
    NutritionModel,
)
from app.infrastructure.data_sources.models.products.product_model import ProductModel
from test.infrastructure.database.data_test_case.database_test_case import (
    DatabaseTestCase,
)
import unittest
import random
import decimal


def create_dto_stub():
    vals = {
        "id": 1,
        "sku": 1,
        "name": "Product",
        "description": "Product Description",
        "image": "Is it mandatory.jpg",
    }

    return ProductDto(**vals)


class TestProductInsertionRepository(DatabaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.sut: ProductInserterRepository = ProductAlchemyRepository(self.session)

    def test_should_add_raw_product(self):
        response = self.sut.create_product(create_dto_stub())

        self.assertIsNotNone(response)

    def test_should_raise_on_integrity_violation(self):
        with self.assertRaises(AlreadyRegisteredProductException):
            self.sut.create_product(create_dto_stub())
            self.sut.create_product(create_dto_stub())

    def test_should_insert_allergen_relationship(self):
        dto = create_dto_stub()
        session = self.session
        with session.begin():
            model = AllergenModel(type="Batata", description="certainly a potato")
            session.add(model)
            model2 = AllergenModel(type="Sundae", description="certainly a sundae")
            session.add(model2)
            session.flush()

            al = self.session.query(AllergenModel).all()

        allergens_dto = map(
            lambda x: {
                "id": x.id,
                "may_have": True,
                "contain": True,
                "description": x.description,
            },
            al,
        )

        allergens: List[ProductAllergenDto] = list(allergens_dto)
        vals = {**dto.dict(), "allergens": allergens}

        response = self.sut.create_product(ProductDto(**vals))

        self.assertIsNotNone(response)

        self.assertEquals(len(response.allergens), 2)

    def test_should_insert_flavour_relationship(self):
        dto = create_dto_stub()
        session = self.session
        with session.begin():
            model = FlavourModel(description="hmmm yammy")
            session.add(model)
            model2 = FlavourModel(description="flavourous")
            session.add(model2)
            session.flush()

            al = self.session.query(FlavourModel).all()

        flavour_dtos = map(
            lambda x: {
                "id": x.id,
                "description": x.description,
            },
            al,
        )

        flavours: List[Flavour] = list(flavour_dtos)

        vals = {**dto.dict(), "flavours": flavours}

        response = self.sut.create_product(ProductDto(**vals))

        self.assertIsNotNone(response)

        self.assertEquals(len(response.flavours), 2)

    def test_should_insert_ingredient_relationship(self):
        dto = create_dto_stub()
        session = self.session
        with session.begin():
            model = IngredientModel(name="salt")
            session.add(model)
            model2 = IngredientModel(name="sea")
            session.add(model2)
            session.flush()

            al = self.session.query(IngredientModel).all()

        ingredients_dtos = map(
            lambda x: {
                "id": x.id,
                "description": x.name,
            },
            al,
        )

        ingredients: List[ProductIngredient] = list(ingredients_dtos)

        vals = {**dto.dict(), "ingredients": ingredients}

        response = self.sut.create_product(ProductDto(**vals))

        self.assertIsNotNone(response)

        self.assertEquals(len(response.ingredients), 2)

    def test_should_insert_nutrition_relationship(self):
        dto = create_dto_stub()
        session = self.session
        with session.begin():
            model = NutritionModel(description="???")
            session.add(model)
            model2 = NutritionModel(description="nutrient")
            session.add(model2)
            session.flush()

            al = self.session.query(NutritionModel).all()

        nutrition_dtos = map(
            lambda x: {
                "key": x.id,
                "value": decimal.Decimal(random.randrange(155, 389)) / 100,
            },
            al,
        )

        nutritions: List[ProductNutrition] = list(nutrition_dtos)

        vals = {**dto.dict(), "nutrition": nutritions}

        response = self.sut.create_product(ProductDto(**vals))

        self.assertIsNotNone(response)

        self.assertEquals(len(response.nutrition), 2)

    def test_should_retrieve_product_after_insertion(self):
        self.sut.create_product(create_dto_stub())

        product = self.session.query(ProductModel).get(1)

        self.assertIsNotNone(product)
        assert product.id == 1


if __name__ == "__main__":
    unittest.main()
