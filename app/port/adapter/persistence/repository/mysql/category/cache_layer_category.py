from typing import Optional

from cachetools import TTLCache, cached
from injector import inject

from domain.model.category import CategoryId, Category
from port.adapter.persistence.repository.mysql.category import DriverManagerCategory


class CacheLayerCategory:
    """ローカルキャッシュを保持するクラス"""
    # 60秒 × 15分
    __TTL = 60 * 15

    @inject
    def __init__(self, driver_manager_category: DriverManagerCategory):
        self.__driver_manager_category = driver_manager_category

    @cached(cache=TTLCache(maxsize=128, ttl=__TTL))
    def categories_or_origin(self, category_ids: set[CategoryId]) -> set[Category]:
        return self.__driver_manager_category.find_by_ids(category_ids)

    @cached(cache=TTLCache(maxsize=128, ttl=__TTL))
    def category_or_origin(self, category_id: CategoryId) -> Optional[Category]:
        return self.__driver_manager_category.find_by_id(category_id)
