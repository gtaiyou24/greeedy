from typing import Optional, Set

from injector import singleton, inject

from application.item.dpo import SearchHitItemsDpo
from domain.model.gender import Gender
from domain.model.item import ItemIndex


@singleton
class SearchItemApplicationService:
    @inject
    def __init__(self, item_index: ItemIndex):
        self.__item_index = item_index

    def search(self,
               gender: str, text: Optional[str], category: Optional[str],
               colors: Set[str], designs: Set[str], details: Set[str],
               price_from: Optional[int], price_to: Optional[int],
               sort: str, start: int, size: int) -> SearchHitItemsDpo:
        search_hit_items = self.__item_index.search(Gender[gender], text, category, colors, designs, details,
                                                    price_from, price_to, sort, start, size)
        return SearchHitItemsDpo(search_hit_items.total_results_available, search_hit_items.hits)
