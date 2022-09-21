from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from application.category.dpo import GetCategoryTreeDpo


class GetCategoryTreeListJson(BaseModel):
    class CategoryTree(BaseModel):
        id: str = Field(title="カテゴリID")
        name: str = Field(title="カテゴリ名")
        image: str = Field(title="画像URL")
        sub_categories: List[CategoryTree] = Field(default=[], title="サブカテゴリ一覧")

        @staticmethod
        def make_by(category_tree: GetCategoryTreeDpo.CategoryTreeDpo) -> GetCategoryTreeListJson.CategoryTree:
            return GetCategoryTreeListJson.CategoryTree(
                id=category_tree.current_category.id.value,
                name=category_tree.current_category.name.text,
                image=category_tree.current_category.image_url.address,
                sub_categories=[GetCategoryTreeListJson.CategoryTree.make_by(child_category_tree) \
                                for child_category_tree in category_tree.sub_category_list])

    categories: List[GetCategoryTreeListJson.CategoryTree] = Field(default=[], title="カテゴリツリー一覧")

    @staticmethod
    def make_by(dpo: GetCategoryTreeDpo) -> GetCategoryTreeListJson:
        return GetCategoryTreeListJson(
            categories=[GetCategoryTreeListJson.CategoryTree.make_by(category_tree) for category_tree in dpo.list])
