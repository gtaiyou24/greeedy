from __future__ import annotations

from typing import List

from sqlalchemy import Column, VARCHAR, Integer, ForeignKey

from domain.model.category import Category, CategoryTree, CategoryId
from port.adapter.persistence.repository.mysql import Base


class CategoryRelationsTableRow(Base):
    __tablename__ = "category_relations"
    __table_args__ = ({"mysql_charset": "utf8mb4", "mysql_engine": "InnoDB"})

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    parent_category_id = Column(VARCHAR(255), ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    child_category_id = Column(VARCHAR(255), ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    sort_order = Column(Integer, nullable=False)

    @staticmethod
    def of(category: Category) -> List[CategoryRelationsTableRow]:
        return [
            CategoryRelationsTableRow(parent_category_id=category.id.value,
                                      child_category_id=sub_category_id.value,
                                      sort_order=i) \
            for i, sub_category_id in enumerate(category.sub_category_ids, start=1)
        ]
