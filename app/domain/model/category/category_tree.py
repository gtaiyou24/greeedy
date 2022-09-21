from __future__ import annotations

from dataclasses import dataclass

from domain.model.category import CategoryId


@dataclass(init=False, unsafe_hash=True, frozen=True)
class CategoryTree:
    current: CategoryId
    children: list[CategoryTree]

    def __init__(self, current: CategoryId, children: list[CategoryTree]):
        assert isinstance(current, CategoryId), "currentにはCategoryIdを指定してください。(type={})".format(type(current))
        assert isinstance(children, list), "childrenにはlist[CategoryTree]を指定してください。(type={})".format(type(children))
        super().__setattr__("current", current)
        super().__setattr__("children", children)

    def has(self, category_id: CategoryId) -> bool:
        if self.current == category_id:
            return True
        for child in self.children:
            if child.has(category_id):
                return True
        return False

    def all_category_ids(self) -> set[CategoryId]:
        category_ids = {self.current}
        category_trees = list(self.children)
        while True:
            if not category_trees:
                break
            a_category_tree = category_trees.pop()
            category_ids.add(a_category_tree.current)
            for c in a_category_tree.children:
                category_trees.append(c)
        return set(category_ids)
