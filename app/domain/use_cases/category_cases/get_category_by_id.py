from abc import ABC, abstractmethod
from app.domain.entities.category import Category


class GetCategoryById(ABC):
    @abstractmethod
    def get_category_by_id(self, id: int) -> Category:
        pass