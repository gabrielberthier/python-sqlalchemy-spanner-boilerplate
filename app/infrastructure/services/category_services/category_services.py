from unicodedata import category
from fastapi.exceptions import HTTPException
from app.domain.entities.category import Category, CategoryDto, CategoryUpdateDto
from app.domain.repositories.category.category_repository import CategoryRepository
from app.domain.use_cases.category_cases.create_category import CreateCategory
from app.domain.use_cases.category_cases.get_category_by_id import GetCategoryById
from app.domain.use_cases.category_cases.update_category import UpdateCategory
from app.framework.schemas.category import CategorySchema, CategoryUpdateSchema
from app.infrastructure.data_sources.adapter_repositories.category.category_alchemy_repository import (
    AlreadyRegisteredCategoryException,
    InvalidSkuException,
    NoParentCategoryException,
)


class CategoryService(CreateCategory, GetCategoryById, UpdateCategory):
    def __init__(self, repository: CategoryRepository) -> None:
        self.repository = repository

    def create_category(self, command: CategorySchema) -> Category:
        try:
            return self.repository.create_category(CategoryDto(**command.dict()))
        except AlreadyRegisteredCategoryException:
            raise HTTPException(status_code=400, detail="Category already registered")
        except NoParentCategoryException as e:
            raise HTTPException(
                status_code=400, detail="The parent category does not exist"
            )
        except InvalidSkuException as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_category_by_id(self, id: int) -> Category:
        category = self.repository.get_category(id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category

    def update_category(self, id: int, command: CategoryUpdateSchema) -> Category:
        category = self.repository.update_category(id, command)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")
        return category
