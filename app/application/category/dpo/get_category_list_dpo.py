from dataclasses import dataclass

from domain.model.category import Category


@dataclass(unsafe_hash=True, frozen=True)
class GetCategoryListDpo:
    category_list: list[Category]
