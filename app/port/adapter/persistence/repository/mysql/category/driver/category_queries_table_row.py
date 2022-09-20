from __future__ import annotations

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
        return CategoryQueriesTableRow(
            category_id=category.id.value,
            queries={operator.name: {q.operator.name: q.text for q in query_set} for operator, query_set in category.query_set.all.items()}
        )

    def to_query_set(self) -> QuerySet:
        return QuerySet({Operator[operator]: {Query(text, Operator[o]) for o, text in queries.items()} \
                         for operator, queries in self.queries.items()})
