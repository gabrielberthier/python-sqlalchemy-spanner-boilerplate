from app.domain.entities.ingredients.ingredient import (
    Ingredient,
    IngredientDto,
    UpdateIngredient,
)
from app.domain.repositories.ingredients.ingredients_repository import (
    IngredientsRepository,
)
from app.infrastructure.data_sources.adapter_repositories.ingredients.ingredients_alchemy_repository import (
    IngredientsAlchemyRepository,
)
from test.infrastructure.database.data_test_case.database_test_case import (
    DatabaseTestCase,
)
from unittest import main
import app.infrastructure.data_sources.models.products.product_model
import app.infrastructure.data_sources.models.allergens.allergen_presence_model
import app.infrastructure.data_sources.models.allergens.allergen_model


def ingredient_factory() -> IngredientDto:
    vals = {
        "name": "Celoglobiol",
    }
    return IngredientDto(**vals)


def update_ingredient_factory() -> IngredientDto:
    valsToUpdate = {
        "name": "mostarda",
    }
    return UpdateIngredient(**valsToUpdate)


class TestIngredientRepository(DatabaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.sut: IngredientsRepository = IngredientsAlchemyRepository(self.session)

    def test_can_insert(self):
        ingredient = self.sut.add_ingredient(ingredient_factory())

        assert ingredient.id == 1

    def test_should_insert_many_records(self):
        i_list = []
        for i in range(0, 10):
            i_list.append(ingredient_factory())
        response = self.sut.add_ingredients(i_list)

        self.assertGreater(len(response), 0)

    def test_should_find_by_id(self):
        self.sut.add_ingredient(ingredient_factory())

        ingredient = self.sut.get_ingredient(1)

        self.assertIsNotNone(ingredient)

    def test_should_delete_by_id(self):
        self.sut.add_ingredient(ingredient_factory())

        ingredient = self.sut.delete_ingredient(1)
        print(ingredient)
        self.assertIsNotNone(ingredient)

    def test_should_update_by_id(self):
        self.sut.add_ingredient(ingredient_factory())

        ingredient = self.sut.update_ingredient(update_ingredient_factory())
        print(ingredient)
        self.assertIsNotNone(ingredient)


if __name__ == "__main__":
    main()
