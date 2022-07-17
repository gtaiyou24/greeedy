from typing import Optional, List

from injector import inject

from domain.model.item import ItemRepository, Item
from domain.model.item.id import ItemId
from port.adapter.persistence.repository.mysql.item import CacheLayerItem, DriverManagerItem


class MySQLItemRepository(ItemRepository):

    @inject
    def __init__(self, cache_layer_item: CacheLayerItem,
                 driver_manager_item: DriverManagerItem):
        self.__cache_layer_item = cache_layer_item
        self.__driver_manager_item = driver_manager_item

    def save(self, item: Item):
        self.__driver_manager_item.upsert(item)

    def item_of(self, id: ItemId) -> Optional[Item]:
        return self.__cache_layer_item.item_or_origin(id)

    def items_of(self, ids: List[ItemId]) -> List[Item]:
        return self.__cache_layer_item.items_or_origin(ids)

    def delete(self, id: ItemId):
        self.__driver_manager_item.delete(id)
