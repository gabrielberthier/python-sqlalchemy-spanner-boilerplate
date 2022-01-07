from abc import ABC, abstractmethod
from app.domain.entities.category import Category
from app.framework.schemas.category import CategoryUpdateSchema


class UpdateCategory(ABC):
    @abstractmethod
    def update_category(self, id: int, command: CategoryUpdateSchema) ->Category:
        pass
