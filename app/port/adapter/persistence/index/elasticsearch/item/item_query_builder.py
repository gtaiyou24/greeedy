from __future__ import annotations

from typing import Optional, Set

from elasticsearch_dsl import Q

from domain.model.category import Category
from domain.model.color import Color
from domain.model.gender import Gender
from domain.model.query import Operator


class ItemQueryBuilder:
    bool_type = {Operator.AND: 'must', Operator.OR: 'should', Operator.NOT: 'must_not'}

    text_fields = ['name^2', 'name.gram', 'brand_name^2', 'keywords', 'description', 'description.ngram', 'content', 'content.ngram']
    category_fields = ['name^3', 'keywords']
    designs_fields = ["name^3", "keywords", "description", "content^2"]
    details_fields = ["name^3", "keywords^2", "description^2", "content^2"]
    colors_fields = ["name", "name.ngram", "keywords", "description", "description.ngram", "content", "content.ngram"]

    def __init__(self):
        self.__must = []
        self.__filter = []

    def __multi_match(self, query: str, fields: list[str], operator: str = 'or') -> Q:
        return Q('multi_match', query=query, fields=fields, operator=operator)

    def text(self, text: Optional[str]) -> ItemQueryBuilder:
        if text:
            self.__must.append(self.__multi_match(text, self.text_fields))
        return self

    def category(self, category: Optional[Category]) -> ItemQueryBuilder:
        if category:
            _bool = {}
            for operator, queries in category.query_set.all.items():
                _bool[self.bool_type[operator]] = [
                    self.__multi_match(q.text, self.category_fields, q.operator.value) for q in queries
                ]
            self.__must.append(Q('bool', **_bool))
        return self

    def designs(self, designs: Set[str]) -> ItemQueryBuilder:
        if designs:
            self.__must.append(self.__multi_match(' '.join(designs), self.designs_fields))
        return self

    def details(self, details: Set[str]) -> ItemQueryBuilder:
        if details:
            self.__must.append(self.__multi_match(' '.join(details), self.details_fields))
        return self

    def gender(self, gender: Gender) -> ItemQueryBuilder:
        self.__filter.append(Q('term', gender=gender.name))
        return self

    def colors(self, colors: Set[Color]) -> ItemQueryBuilder:
        if colors:
            self.__filter.append(self.__multi_match(' '.join([color.value for color in colors]), self.colors_fields))
        return self

    def price(self, price_from: Optional[int], price_to: Optional[int]) -> ItemQueryBuilder:
        if price_from and price_to:
            self.__filter.append(Q('range', price={'gte': price_from, 'lte': price_to}))
        elif price_from:
            self.__filter.append(Q('range', price={'gte': price_from}))
        elif price_to:
            self.__filter.append(Q('range', price={'lte': price_to}))
        return self

    def build(self) -> Q:
        return Q('bool', must=self.__must, filter=self.__filter)
