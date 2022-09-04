from typing import Optional, Set

from injector import singleton, inject

from application.item.dpo import SearchHitItemsDpo
from domain.model.category import CategoryId, CategoryRepository
from domain.model.color import Color
from domain.model.gender import Gender
from domain.model.item import ItemIndex
from exception import SystemException, ErrorCode


@singleton
class SearchItemApplicationService:
    @inject
    def __init__(self, item_index: ItemIndex, category_repository: CategoryRepository):
        self.__item_index = item_index
        self.__category_repository = category_repository

    def search(self,
               a_gender: str, text: Optional[str], a_category_id: Optional[str],
               colors: Set[str], designs: Set[str], details: Set[str],
               price_from: Optional[int], price_to: Optional[int],
               sort: str, start: int, size: int) -> SearchHitItemsDpo:
        gender = Gender[a_gender]
        colors = set([Color.value_of(color) for color in colors])

        category = None
        if a_category_id:
            category_id = CategoryId(a_category_id)
            category = self.__category_repository.category_of(category_id)
            if category is None:
                raise SystemException(
                    ErrorCode.CATEGORY_NOT_FOUND, 'カテゴリID {} のカテゴリが見つかりませんでした'.format(category_id.value))

        search_hit_items = self.__item_index.search(gender, text, category, colors, designs, details,
                                                    price_from, price_to, sort, start, size)
        return SearchHitItemsDpo(search_hit_items.total_results_available, search_hit_items.hits)
