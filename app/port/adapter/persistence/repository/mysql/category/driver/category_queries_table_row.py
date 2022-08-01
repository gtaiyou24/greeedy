from __future__ import annotations

from sqlalchemy import Column, VARCHAR, func, DateTime, Integer, ForeignKey, JSON
from sqlalchemy.orm import declarative_base

from domain.model.category import Category

BaseForCategoryQueries = declarative_base()


class CategoryQueriesTableRow(BaseForCategoryQueries):
    __tablename__ = "category_queries"
    __table_args__ = ({"mysql_charset": "utf8mb4", "mysql_engine": "InnoDB"})

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    category_id = Column(VARCHAR(255), ForeignKey("categories.id", ondelete="CASCADE", nullable=False))
    queries = Column(JSON(), default={}, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    @staticmethod
    def of(category: Category) -> CategoryQueriesTableRow:
        return CategoryQueriesTableRow(
            category_id=category.id,
            queries={operator.name: {q.operator: q.text for q in query_set} for operator, query_set in category.query_set.all.items()}
        )
