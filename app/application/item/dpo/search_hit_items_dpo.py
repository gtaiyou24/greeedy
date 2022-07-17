from __future__ import annotations

from dataclasses import dataclass
from typing import List

from domain.model.item import Item


@dataclass(unsafe_hash=True, frozen=True)
class SearchHitItemsDpo:
    total_results_available: int
    list: List[Item]
