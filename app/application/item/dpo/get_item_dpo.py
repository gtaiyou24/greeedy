from dataclasses import dataclass

from domain.model.item import Item


@dataclass(unsafe_hash=True, frozen=True)
class GetItemDpo:
    item: Item
