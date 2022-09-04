import abc
from typing import Optional, Set, NoReturn

from domain.model.category import Category
from domain.model.color import Color
from domain.model.gender import Gender
from domain.model.item import SearchHitItems
from domain.model.item.id import ItemId
from domain.model.item.item import Item


class ItemIndex(abc.ABC):
    @abc.abstractmethod
    def add(self, item: Item) -> NoReturn:
        pass

    @abc.abstractmethod
    def get(self, item_id: ItemId) -> Optional[Item]:
        pass

    @abc.abstractmethod
    def delete(self, item_id: ItemId) -> NoReturn:
        pass

    @abc.abstractmethod
    def search(self, gender: Gender, text: Optional[str],
               category: Optional[Category], colors: Set[Color],
               designs: Set[str], details: Set[str],
               price_from: Optional[int], price_to: Optional[int],
               sort: str = "relevance", start: int = 1, size: int = 20) -> SearchHitItems:
        pass
