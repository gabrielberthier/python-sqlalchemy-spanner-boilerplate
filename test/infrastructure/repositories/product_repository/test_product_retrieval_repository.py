from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import true
from sqlalchemy.sql.functions import random
from app.domain.entities.flavour.flavour import Flavour
from app.domain.entities.ingredients.ingredient import IngredientDto
from app.domain.entities.product.product import ProductDto
from app.domain.entities.product.product_allergen import ProductAllergenDto
from app.domain.entities.product.product_ingredient import ProductIngredient
from app.domain.entities.product.product_nutrition import ProductNutrition
from app.domain.repositories.product.product_getter_repository import (
    ProductGetterRepository,
)
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


def create_dto_stub(session: Session):
    vals = {
        "id": 1,
        "sku": 1,
        "name": "Product",
        "description": "Product Description",
        "image": "Is it mandatory.jpg",
        "allergens": construct_allergens_dtos(session),
        "flavours": construct_flavours_dtos(session),
        "ingredients": construct_ingredients_dtos(session),
        "nutrition": construct_nutrition_dtos(session),
    }

    return ProductDto(**vals)


def insert_dependencies(session: Session):
    with session.begin():
        model = AllergenModel(type="Batata", description="certainly a potato")
        session.add(model)
        model2 = AllergenModel(type="Sundae", description="certainly a sundae")
        session.add(model2)
        model = FlavourModel(description="hmmm yammy")
        session.add(model)
        model2 = FlavourModel(description="flavourous")
        session.add(model2)
        model = IngredientModel(name="salt")
        session.add(model)
        model2 = IngredientModel(name="sea")
        session.add(model2)
        model = NutritionModel(description="???")
        session.add(model)
        model2 = NutritionModel(description="nutrient")
        session.add(model2)


def construct_allergens_dtos(session: Session):
    al = session.query(AllergenModel).all()
    allergens_dto = map(
        lambda x: {
            "id": x.id,
            "may_have": True,
            "contain": True,
            "description": x.description,
        },
        al,
    )

    return list(allergens_dto)


def construct_flavours_dtos(session: Session):
    al = session.query(FlavourModel).all()
    flavour_dtos = map(
        lambda x: {
            "id": x.id,
            "description": x.description,
        },
        al,
    )

    return list(flavour_dtos)


def construct_ingredients_dtos(session: Session):
    al = session.query(IngredientModel).all()

    ingredients_dtos = map(
        lambda x: {
            "id": x.id,
            "description": x.name,
        },
        al,
    )

    return list(ingredients_dtos)


def construct_nutrition_dtos(session: Session):
    al = session.query(NutritionModel).all()

    nutrition_dtos = map(
        lambda x: {
            "key": x.id,
            "value": decimal.Decimal(random.randrange(155, 389)) / 100,
        },
        al,
    )

    return list(nutrition_dtos)


class TestProductRetrievalRepository(DatabaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        insert_dependencies(self.session)

        self.sut: ProductGetterRepository = ProductAlchemyRepository(self.session)
        blub: ProductInserterRepository = ProductAlchemyRepository(self.session)
        blub.create_product(create_dto_stub(self.session))

    def test_retrieve_entities(self):
        product = self.sut.get_product(1)
        self.assertIsNotNone(product)

        self.assertEquals(len(product.flavours), 2)
        self.assertEquals(len(product.ingredients), 2)
        self.assertEquals(len(product.nutrition), 2)
        self.assertEquals(len(product.allergens), 2)


if __name__ == "__main__":
    unittest.main()
