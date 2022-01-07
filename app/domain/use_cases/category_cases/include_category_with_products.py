from abc import ABC, abstractmethod
from app.domain.entities.category import Category
from app.framework.schemas.category import CategorySchema


class IncludeCategoryWithProducts(ABC):
    @abstractmethod
    def create_category(self, command: CategorySchema) -> Category:
        pass
