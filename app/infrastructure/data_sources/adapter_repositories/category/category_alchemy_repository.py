import traceback
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session
from app.domain.entities.category import Category, CategoryDto, CategoryUpdateDto
from app.domain.entities.product.product import Product
from app.domain.repositories.category.category_repository import CategoryRepository
from app.infrastructure.data_sources.models.categories.category_model import (
    CategoryModel,
)
from app.infrastructure.data_sources.models.products.product_model import ProductModel


class AlreadyRegisteredCategoryException(Exception):
    pass


class NoParentCategoryException(Exception):
    pass


class InvalidSkuException(Exception):
    def __init__(self, sku):
        self.message = f"The product with sku [{sku}] does not exist"
        super().__init__(self.message)


class CategoryAlchemyRepository(CategoryRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_category(self, id: int) -> Category:
        model = self.db.query(CategoryModel).filter(CategoryModel.plk_id == id).first()
        if not model:
            return None
        products: List[Product] = []
        for product in model.products:
            products.append(Product(**product.__dict__))
        values = {**model.__dict__, "products": products}
        return Category(**values)

    def create_category(self, category: CategoryDto) -> Category:
        cat_vals = category.dict()
        cat_vals["plk_id"] = cat_vals.pop("id")
        vals = {**cat_vals}
        skus = vals.pop("skus")
        model = CategoryModel(**vals)
        products: List[Product] = []
        if vals["parent_category"] and not self.db.query(CategoryModel).get(
            category.parent_category
        ):
            raise NoParentCategoryException

        for sku in skus:
            product_model = (
                self.db.query(ProductModel).filter(ProductModel.sku == sku).first()
            )
            if not product_model:
                raise InvalidSkuException(sku)
            model.products.append(product_model)
            products.append(Product(**product_model.__dict__))
        try:
            self.db.add(model)

            self.db.commit()
            self.db.refresh(model)
            values = {**model.__dict__, "products": products}

            return Category(**values)
        except IntegrityError:
            self.db.rollback()
            raise AlreadyRegisteredCategoryException
        except Exception as ex:
            print(ex)
            traceback.print_exc()
            self.db.rollback()

    def update_category(self, id: int, category: CategoryUpdateDto) -> Category:
        model = self.get_category(id)
        if model:
            model.name = category.name
            model.image_url = category.image_url
            model.display_order = category.display_order
            model.color = category.color
            model.parent_category = category.parent_category
        self.db.commit()
        self.db.refresh()
        return Category(**model.__dict__)
