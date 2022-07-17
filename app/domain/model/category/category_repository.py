import abc
from typing import List, Optional

from domain.model.category import CategoryTree, CategoryId, Category
from domain.model.gender import Gender


class CategoryRepository(abc.ABC):
    @abc.abstractmethod
    def category_tree(self, gender: Gender) -> List[CategoryTree]:
        pass

    @abc.abstractmethod
    def category_of(self, category_id: CategoryId) -> Optional[Category]:
        pass
