from abc import ABC, abstractmethod
from app.domain.entities.category import Category, CategoryDto, CategoryUpdateDto


class CategoryRepository(ABC):
    @abstractmethod
    def create_category(self, category: CategoryDto) -> Category:
        pass

    @abstractmethod
    def get_category(self, id: int) -> Category:
        pass

    @abstractmethod
    def update_category(self, id: int, category: CategoryUpdateDto) -> Category:
        pass
