from dataclasses import dataclass
from typing import List

from domain.model.item import Item


@dataclass(unsafe_hash=True, frozen=True)
class GetItemListDpo:
    items: List[Item]
