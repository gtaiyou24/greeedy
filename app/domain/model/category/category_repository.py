import abc
from typing import Optional, NoReturn

from domain.model.category import CategoryTree, CategoryId, Category


class CategoryRepository(abc.ABC):
    @abc.abstractmethod
    def category_tree_of(self, category_id: CategoryId) -> CategoryTree:
        pass

    @abc.abstractmethod
    def categories_of(self, category_ids: set[CategoryId]) -> set[Category]:
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
