import abc
from typing import List, Optional

from domain.model.item import Item
from domain.model.item.id import ItemId


class ItemRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, item: Item):
        pass

    @abc.abstractmethod
    def item_of(self, id: ItemId) -> Optional[Item]:
        pass

    @abc.abstractmethod
    def items_of(self, ids: List[ItemId]) -> List[Item]:
        pass

    @abc.abstractmethod
    def delete(self, id: ItemId):
        pass
