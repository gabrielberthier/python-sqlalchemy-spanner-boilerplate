from fastapi import APIRouter, Depends
from app.domain.entities.category import Category
from app.domain.use_cases.category_cases.create_category import CreateCategory
from app.domain.use_cases.category_cases.get_category_by_id import GetCategoryById
from app.domain.use_cases.category_cases.update_category import UpdateCategory
from app.framework.factories.category_factories.category_services_factories import (
    category_finder_factory,
    category_inserter_factory,
    category_updater_factory,
)
from app.framework.schemas.category import CategorySchema, CategoryUpdateSchema


router = APIRouter()


@router.post("/category", response_model=Category)
async def post_category(
    category: CategorySchema,
    service: CreateCategory = Depends(category_inserter_factory),
):

    return service.create_category(category)


@router.get("/category/{id}", response_model=Category)
async def get_category(
    id: int, service: GetCategoryById = Depends(category_finder_factory)
):

    return service.get_category_by_id(id)


@router.put("/category", response_model=Category)
async def update_category(
    id: int,
    category: CategoryUpdateSchema,
    service: UpdateCategory = Depends(category_updater_factory),
):

    return service.update_category(id, category)
