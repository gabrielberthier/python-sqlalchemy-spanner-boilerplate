from app.domain.entities.product.product import Product
from app.infrastructure.data_sources.models.allergens.allergen_model import (
    AllergenModel,
)
from app.infrastructure.data_sources.models.allergens.allergen_presence_model import (
    AllergenPresence,
)
from app.infrastructure.data_sources.models.ingredients.ingredient_presence_model import (
    IngredientPresence,
)

from app.infrastructure.data_sources.models.products.product_model import ProductModel
from .data_test_case.database_test_case import DatabaseTestCase
from unittest import main


class TestAllergenModel(DatabaseTestCase):
    def test_can_insert(self):
        session = self.session
        model = AllergenModel(type="Batata", description="certainly a potato")
        session.add(model)
        session.commit()
        session.refresh(model)

        assert model.id == 1

    def test_should_get_all_allergens(self):
        session = self.session
        model = AllergenModel(type="Batata", description="certainly a potato")
        session.add(model)
        model = AllergenModel(type="Amendoim", description="certainly a nut")
        session.add(model)
        session.commit()

        all = session.query(AllergenModel).all()

        self.assertIsNotNone(all)
        self.assertGreater(len(all), 0)

        assert all[1].type == "Amendoim"

    def test_should_insert_throught_product(self):
        allergen_presence = AllergenPresence(
            description="", may_have=True, contain=False
        )
        product = ProductModel(
            sku=3,
            name="Burgão",
            description="Um belo burger",
            image="path/to/image.png",
            combo=None,
        )
        print(product.__dict__)
        model = AllergenModel(type="Batata", description="certainly a potato")
        allergen_presence.allergen = model
        product.allergens.append(allergen_presence)
        session = self.session
        session.add(product)
        session.commit()
        session.refresh(product)

        print(product.__dict__)


if __name__ == "__main__":
    main()
