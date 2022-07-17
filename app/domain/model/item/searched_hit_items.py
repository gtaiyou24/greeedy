from dataclasses import dataclass
from typing import List

from domain.model.item import Item


@dataclass(init=False, unsafe_hash=True, frozen=True)
class SearchHitItems:
    total_results_available: int
    hits: List[Item]

    def __init__(self, total_results_available: int, hits: List[Item]):
        assert isinstance(total_results_available, int) and total_results_available is not None, "総検索ヒット件数は必須です"
        assert total_results_available >= 0, "総検索ヒット件数には0以上の値を指定してください"
        assert isinstance(hits, List), "ヒット一覧は必須です"
        super().__setattr__("total_results_available", total_results_available)
        super().__setattr__("hits", hits)
