from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.domain.use_cases.category_cases.create_category import CreateCategory
from app.domain.use_cases.category_cases.get_category_by_id import GetCategoryById
from app.domain.use_cases.category_cases.update_category import UpdateCategory
from app.infrastructure.data_sources.adapter_repositories.category.category_alchemy_repository import (
    CategoryAlchemyRepository,
)
from app.infrastructure.database.db import get_db
from app.infrastructure.services.category_services.category_services import CategoryService


def category_inserter_factory(db: Session = Depends(get_db)) -> CreateCategory:
    service: CreateCategory = CategoryService(CategoryAlchemyRepository(db))
    return service


def category_finder_factory(db: Session = Depends(get_db)) -> GetCategoryById:
    service: GetCategoryById = CategoryService(CategoryAlchemyRepository(db))
    return service

def category_updater_factory(db: Session = Depends(get_db)) -> UpdateCategory:
    service: UpdateCategory = CategoryService(CategoryAlchemyRepository(db))
    return service
