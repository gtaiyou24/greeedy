from __future__ import annotations

from sqlalchemy import Column, DateTime, func, TEXT, VARCHAR

from domain.model.category import Category
from port.adapter.persistence.repository.mysql import Base


class CategoriesTableRow(Base):
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
