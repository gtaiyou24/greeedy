import abc
from hashlib import sha256
from typing import Any

from domain.model.item.id import ItemId


class ItemIdFactory(abc.ABC):

    @abc.abstractmethod
    def make(self, value: Any) -> ItemId:
        pass


class ItemIdFactoryImpl(ItemIdFactory):
    def make(self, value: str) -> ItemId:
        return ItemId(sha256(value.encode('utf-8')).hexdigest())
