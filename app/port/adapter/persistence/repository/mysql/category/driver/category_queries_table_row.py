from __future__ import annotations

from typing import NoReturn

from sqlalchemy import Column, VARCHAR, func, DateTime, Integer, ForeignKey, JSON

from domain.model.category import Category
from domain.model.query import QuerySet, Operator, Query
from port.adapter.persistence.repository.mysql import Base


class CategoryQueriesTableRow(Base):
    __tablename__ = "category_queries"
    __table_args__ = ({"mysql_charset": "utf8mb4", "mysql_engine": "InnoDB"})

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    category_id = Column(VARCHAR(255), ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    queries = Column(JSON(), default={}, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    @staticmethod
    def of(category: Category) -> CategoryQueriesTableRow:
        queries = {}
        for operator, query_set in category.query_set.all.items():
            query_list = list()
            for query in query_set:
                query_list.append({'text': query.text, 'operator': query.operator.name})
            queries[operator.name] = query_list

        return CategoryQueriesTableRow(category_id=category.id.value, queries=queries)

    def update(self, category_queries_table_row: CategoryQueriesTableRow) -> NoReturn:
        self.category_id = category_queries_table_row.category_id
        self.queries = category_queries_table_row.queries

    def to_query_set(self) -> QuerySet:
        return QuerySet({Operator[operator]: {Query(query['text'], Operator[query['operator']]) for query in query_list} \
                         for operator, query_list in self.queries.items()})
