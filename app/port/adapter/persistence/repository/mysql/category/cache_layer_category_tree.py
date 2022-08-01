from typing import List

from cachetools import cached, TTLCache
from injector import inject

from domain.model.category import CategoryTree
from domain.model.gender import Gender
from port.adapter.persistence.repository.mysql.category import DriverManagerCategoryTree


class CacheLayerCategoryTree:
    """ローカルキャッシュを保持するクラス"""
    # 60秒 × 15分
    __TTL = 60 * 15

    @inject
    def __init__(self, driver_manager_category_tree: DriverManagerCategoryTree):
        self.__driver_manager_category_tree = driver_manager_category_tree

    @cached(cache=TTLCache(maxsize=128, ttl=__TTL))
    def category_tree_list_or_origin(self, gender: Gender) -> List[CategoryTree]:
        return self.__driver_manager_category_tree.find_list_by_gender(gender)
