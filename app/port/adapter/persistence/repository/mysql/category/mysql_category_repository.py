from typing import Optional, NoReturn

from injector import inject

from domain.model.category import CategoryRepository, CategoryTree, CategoryId, Category
from port.adapter.persistence.repository.mysql.category import CacheLayerCategory, DriverManagerCategory, \
    CacheLayerCategoryTree


class MySQLCategoryRepository(CategoryRepository):
    @inject
    def __init__(self,
                 cache_layer_category: CacheLayerCategory,
                 cache_layer_category_tree: CacheLayerCategoryTree,
                 driver_manager_category: DriverManagerCategory):
        self.__cache_layer_category = cache_layer_category
        self.__cache_layer_category_tree = cache_layer_category_tree
        self.__driver_manager_category = driver_manager_category

    def category_tree_of(self, category_id: CategoryId) -> CategoryTree:
        return self.__cache_layer_category_tree.category_tree_or_origin(category_id)

    def categories_of(self, category_ids: set[CategoryId]) -> set[Category]:
        return set({self.__cache_layer_category.category_or_origin(category_id) for category_id in category_ids})

    def category_list_of(self, start: int, limit: int, sort: str) -> list[Category]:
        return self.__driver_manager_category.find_all(start, limit, sort)

    def category_of(self, category_id: CategoryId) -> Optional[Category]:
        return self.__cache_layer_category.category_or_origin(category_id)

    def save(self, category: Category) -> NoReturn:
        self.__driver_manager_category.upsert(category)

    def delete(self, category_id: CategoryId) -> NoReturn:
        self.__driver_manager_category.delete(category_id)
