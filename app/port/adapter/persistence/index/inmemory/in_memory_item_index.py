from typing import Set, Optional, List

from domain.model.gender import Gender
from domain.model.item import ItemIndex, Item, SearchHitItems
from domain.model.item.id import ItemId


class InMemoryItemIndex(ItemIndex):
    __items: List[Item] = list()

    def add(self, item: Item):
        self.__items.append(item)

    def delete(self, item_id: ItemId):
        [self.__items.remove(item) for item in self.__items if item.id == item_id]

    def search(self, gender: Gender, text: Optional[str],
               category: Set[str], colors: Set[str],
               designs: Set[str], details: Set[str],
               price_from: Optional[int], price_to: Optional[int],
               sort: str, start: int, size: int) -> SearchHitItems:
        return SearchHitItems(len(self.__items), list(self.__items))
