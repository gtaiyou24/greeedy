import abc
from typing import Optional, Set

from domain.model.gender import Gender
from domain.model.item import SearchHitItems
from domain.model.item.id import ItemId
from domain.model.item.item import Item


class ItemIndex(abc.ABC):
    @abc.abstractmethod
    def add(self, item: Item):
        pass

    @abc.abstractmethod
    def delete(self, item_id: ItemId):
        pass

    @abc.abstractmethod
    def search(self, gender: Gender, text: Optional[str],
               category: Optional[str], colors: Set[str],
               designs: Set[str], details: Set[str],
               price_from: Optional[int], price_to: Optional[int],
               sort: str, start: int, size: int) -> SearchHitItems:
        pass
