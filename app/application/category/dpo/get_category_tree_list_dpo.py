from __future__ import annotations

from dataclasses import dataclass
from typing import List

from domain.model.category import Category, CategoryTree


@dataclass(unsafe_hash=True, frozen=True)
class GetCategoryTreeListDpo:
    @dataclass(init=False, unsafe_hash=True, frozen=True)
    class CategoryTree:
        current_category: Category
        sub_category_list: List[GetCategoryTreeListDpo.CategoryTree]

        def __init__(self, category_tree: CategoryTree):
            super().__setattr__("current_category", category_tree.current)
            super().__setattr__("sub_category_list", [GetCategoryTreeListDpo.CategoryTree(child) for child in category_tree.children])

    list: List[GetCategoryTreeListDpo.CategoryTree]

    def __init__(self, list: List[CategoryTree]):
        super().__setattr__("list", [GetCategoryTreeListDpo.CategoryTree(category_tree) for category_tree in list])
