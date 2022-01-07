from app.infrastructure.data_sources.models.allergens.allergen_model import (
    AllergenModel,
)
from app.infrastructure.data_sources.models.allergens.allergen_presence_model import (
    AllergenPresence,
)
from app.infrastructure.data_sources.models.categories.category_model import (
    CategoryModel,
)
from app.infrastructure.data_sources.models.nutrition.nutrition_info_model import (
    NutritionInfoModel,
)
from app.infrastructure.data_sources.models.nutrition.nutrition_model import (
    NutritionModel,
)
from app.infrastructure.data_sources.models.products.product_model import ProductModel
from .data_test_case.database_test_case import DatabaseTestCase
from unittest import main


class TestNutritionModel(DatabaseTestCase):
    def test_should_throw_when_no_valid_data_is_provided(self):
        with self.assertRaises(Exception) as context:
            model = NutritionModel()
            session = self.session
            session.add(model)
            session.commit()

    def test_can_insert(self):
        session = self.session
        model = NutritionModel(description="Nutritive thing")
        session.add(model)
        session.commit()
        session.refresh(model)

        assert model.id == 1

    def test_should_get_all_nutrients(self):
        session = self.session
        model = NutritionModel(description="Nutritive thing")
        session.add(model)
        model = NutritionModel(description="Nutritive thing but different")
        session.add(model)
        session.commit()

        all = session.query(NutritionModel).all()

        self.assertIsNotNone(all)
        self.assertGreater(len(all), 0)

        assert all[0].description == "Nutritive thing"
        assert all[1].description == "Nutritive thing but different"

    def test_should_insert_throught_product(self):
        model = NutritionModel(description="Nutritive thing but different")
        product = ProductModel(
            sku=3,
            name="Apple",
            description="Aporu",
            image="path/to/image.png",
            combo=None,
        )

        nutrition_info = NutritionInfoModel(value=42)
        nutrition_info.nutrition = model

        product.nutrition_infos.append(nutrition_info)
        session = self.session
        session.add(product)
        session.commit()
        session.refresh(product)

        assert len(product.nutrition_infos) == 1

        product = session.query(ProductModel).get(1)
        for e in product.nutrition_infos:
            assert e.nutrition is not None


if __name__ == "__main__":
    main()
