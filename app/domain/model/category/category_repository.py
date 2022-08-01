import abc
from typing import List, Optional, NoReturn

from domain.model.category import CategoryTree, CategoryId, Category
from domain.model.gender import Gender


class CategoryRepository(abc.ABC):
    @abc.abstractmethod
    def category_tree(self, gender: Gender) -> List[CategoryTree]:
        pass

    @abc.abstractmethod
    def category_of(self, category_id: CategoryId) -> Optional[Category]:
        pass

    @abc.abstractmethod
    def save(self, category: Category) -> NoReturn:
        pass

    @abc.abstractmethod
    def delete(self, category_id: CategoryId) -> NoReturn:
        pass
