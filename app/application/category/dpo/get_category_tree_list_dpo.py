from __future__ import annotations

from dataclasses import dataclass
from typing import List

from domain.model.category import Category, CategoryTree, CategoryId


@dataclass(unsafe_hash=True, frozen=True)
class GetCategoryTreeDpo:
    @dataclass(init=False, unsafe_hash=True, frozen=True)
    class CategoryTreeDpo:
        current_category: Category
        sub_category_list: List[GetCategoryTreeDpo.CategoryTreeDpo]

        def __init__(self, category_tree: CategoryTree, categories: set[Category]):
            super().__setattr__("current_category", self.__current_category_of(category_tree.current, categories))
            super().__setattr__("sub_category_list", [GetCategoryTreeDpo.CategoryTreeDpo(child, categories) \
                                                      for child in category_tree.children])

        def __current_category_of(self, category_id: CategoryId, categories: set[Category]) -> Category:
            for category in categories:
                if category.id == category_id:
                    return category
            ValueError(f'カテゴリID {category_id.value} に該当するカテゴリが見つかりませんでした。')

    list: List[GetCategoryTreeDpo.CategoryTreeDpo]

    def __init__(self, category_tree: CategoryTree, categories: set[Category]):
        super().__setattr__("list", [GetCategoryTreeDpo.CategoryTreeDpo(category_tree, categories) \
                                     for category_tree in category_tree.children])
