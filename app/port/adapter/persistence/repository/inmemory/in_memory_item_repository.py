from slf4py import set_logger
from typing import List, Optional

from domain.model.item import ItemRepository, Item
from domain.model.item.id import ItemId


@set_logger
class InMemoryItemRepository(ItemRepository):
    __items: List[Item] = list()

    def save(self, item: Item):
        self.log.debug("アイテム(ID={})を保存します".format(item.id.value))
        if item not in self.__items:
            self.__items.append(item)

    def item_of(self, id: ItemId) -> Optional[Item]:
        for item in self.__items:
            if item.id == id:
                return item
        return None

    def items_of(self, ids: List[ItemId]) -> List[Item]:
        item_list = list()
        for id in ids:
            item = self.item_of(id)
            if item is None:
                continue
            item_list.append(item)
        return item_list

    def delete(self, id: ItemId):
        [self.__items.remove(item) for item in self.__items if item.id == id]
