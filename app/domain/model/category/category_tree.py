from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional

from domain.model.category import Category, CategoryId


@dataclass(init=False, unsafe_hash=True, frozen=True)
class CategoryTree:
    current: Category
    children: List[CategoryTree]

    def __init__(self, current: Category, children: List[CategoryTree]):
        assert isinstance(current, Category), "currentにはCategoryを指定してください。(type={})".format(type(current))
        assert isinstance(children, List), "childrenにはList[CategoryTree]を指定してください。(type={})".format(type(children))
        super().__setattr__("current", current)
        super().__setattr__("children", children)

    def is_in(self, category_id: CategoryId) -> bool:
        if self.current.id == category_id:
            return True
        for child in self.children:
            if child.is_in(category_id):
                return True
        return False

    def category_of(self, category_id: CategoryId) -> Optional[Category]:
        if self.current.id == category_id:
            return self.current
        for child in self.children:
            optional_category = child.category_of(category_id)
            if optional_category is not None:
                return optional_category
        return None
