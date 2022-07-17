from dataclasses import dataclass
from typing import List

from domain.model.category import CategoryName, CategoryId
from domain.model.gender import Gender
from domain.model.query import QuerySet
from domain.model.url import URL


@dataclass(init=False, eq=False)
class Category:
    id: CategoryId
    gender: Gender
    name: CategoryName
    image_url: URL
    sub_category_ids: List[CategoryId]
    query_set: QuerySet

    def __init__(self, id: CategoryId, gender: Gender, name: CategoryName,
                 image_url: URL, sub_category_ids: List[CategoryId], query_set: QuerySet):
        assert isinstance(id, CategoryId), "カテゴリIDにはCategoryIdを指定してください(type={})".format(type(id))
        assert isinstance(gender, Gender), "ジャンダーにはGenderを指定してください(type={})".format(type(gender))
        assert isinstance(name, CategoryName), "カテゴリ名にはCategoryNameを指定してください(type={})".format(type(name))
        assert isinstance(image_url, URL), "画像URLにはURLを指定してください(type={})".format(type(image_url))
        assert isinstance(sub_category_ids, List), "サブカテゴリにはListを指定してください(type={})".format(type(sub_category_ids))
        assert isinstance(query_set, QuerySet), "クエリセットにはQuerySetを指定してください(type={})".format(type(query_set))
        super().__setattr__("id", id)
        super().__setattr__("gender", gender)
        super().__setattr__("name", name)
        super().__setattr__("image_url", image_url)
        super().__setattr__("sub_category_ids", sub_category_ids)
        super().__setattr__("query_set", query_set)

    def __eq__(self, other):
        if not isinstance(other, Category):
            return False
        return self.id == other.id

    def is_leaf(self) -> bool:
        return self.sub_category_ids == []
