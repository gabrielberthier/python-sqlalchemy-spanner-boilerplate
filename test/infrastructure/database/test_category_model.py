from app.infrastructure.data_sources.models.allergens.allergen_model import (
    AllergenModel,
)
from app.infrastructure.data_sources.models.allergens.allergen_presence_model import (
    AllergenPresence,
)
from app.infrastructure.data_sources.models.categories.category_model import (
    CategoryModel,
)
from app.infrastructure.data_sources.models.products.product_model import ProductModel
from .data_test_case.database_test_case import DatabaseTestCase
from unittest import main


class TestCategoryModel(DatabaseTestCase):
    def test_should_throw_when_no_valid_data_is_provided(self):
        with self.assertRaises(Exception) as context:
            model = CategoryModel()
            session = self.session
            session.add(model)
            session.commit()

    def test_can_insert(self):
        session = self.session
        model = CategoryModel(
            name="Batata",
            image_url="path-to-image",
            display_order=2,
            color="IDK, Blu?",
            parent_category=None,
        )
        session.add(model)
        session.commit()
        session.refresh(model)

        assert model.id == 1

    def test_should_get_all_categories(self):
        session = self.session
        model = CategoryModel(
            name="Batata", image_url="path-to-image", display_order=2, color="IDK, Blu?"
        )
        session.add(model)
        model = CategoryModel(
            name="Catcat", image_url="path-to-image", display_order=2, color="IDK, Red?"
        )
        session.add(model)
        session.commit()

        all = session.query(CategoryModel).all()

        self.assertIsNotNone(all)
        self.assertGreater(len(all), 0)

        assert all[0].name == "Batata"
        assert all[1].name == "Catcat"

    def test_should_insert_throught_product(self):
        category = CategoryModel(
            name="Batata", image_url="path-to-image", display_order=2, color="IDK, Blu?"
        )
        product = ProductModel(
            sku=3,
            name="Batatas fritas com molho",
            description="ba ta ta",
            image="path/to/image.png",
            combo=None,
        )

        product.categories.append(category)
        session = self.session
        session.add(product)
        session.commit()
        session.refresh(product)

        assert len(product.categories) == 1


if __name__ == "__main__":
    main()
