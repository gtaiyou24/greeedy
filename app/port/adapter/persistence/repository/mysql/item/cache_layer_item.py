from typing import Optional, List

from cachetools import TTLCache, cached
from injector import inject

from domain.model.item import Item
from domain.model.item.id import item_id, ItemId
from port.adapter.persistence.repository.mysql.item import DriverManagerItem


class CacheLayerItem:
    """ローカルキャッシュを保持するクラス"""
    # 60秒 × 15分
    __TTL = 60 * 15

    @inject
    def __init__(self, driver_manager_item: DriverManagerItem):
        self.__driver_manager_item = driver_manager_item

    @cached(cache=TTLCache(maxsize=128, ttl=__TTL))
    def item_or_origin(self, id: ItemId) -> Optional[Item]:
        return self.__driver_manager_item.find_by_id(id)

    @cached(cache=TTLCache(maxsize=128, ttl=__TTL))
    def items_or_origin(self, ids: List[ItemId]) -> List[Item]:
        return self.__driver_manager_item.find_all_by_ids(ids)
