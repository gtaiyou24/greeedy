from __future__ import annotations

from typing import List

from sqlalchemy import Column, DateTime, func, TEXT, VARCHAR
from sqlalchemy.orm import declarative_base

from domain.model.category import Category, CategoryId, CategoryName
from domain.model.gender import Gender
from domain.model.url import URL
from port.adapter.persistence.repository.mysql.category.driver import CategoryRelationsTableRow, CategoryQueriesTableRow

BaseForCategories = declarative_base()


class CategoriesTableRow(BaseForCategories):
    __tablename__ = "categories"
    __table_args__ = ({"mysql_charset": "utf8mb4", "mysql_engine": "InnoDB"})

    id = Column(VARCHAR(255), primary_key=True, nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    gender = Column(VARCHAR(10), nullable=False)
    image_url = Column(TEXT, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())

    @staticmethod
    def of(category: Category) -> CategoriesTableRow:
        return CategoriesTableRow(
            id=category.id.value,
            name=category.name.text,
            gender=category.gender.name,
            image_url=category.image_url.address
        )

    def to(self,
           category_queries_table_row: CategoryQueriesTableRow,
           category_relations_table_row_list: List[CategoryRelationsTableRow]) -> Category:
        return Category(
            CategoryId(self.id), Gender[self.gender], CategoryName(self.name), URL(self.image_url),
            [CategoryId(t.child_category_id) for t in category_relations_table_row_list],
            # QuerySet(category_queries_table_row.queries)
        )
