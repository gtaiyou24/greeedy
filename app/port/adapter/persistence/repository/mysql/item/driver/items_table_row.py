from __future__ import annotations

from sqlalchemy import Column, DateTime, func, TEXT, VARCHAR, Integer, Boolean
from sqlalchemy.orm import declarative_base

BaseForItems = declarative_base()


class ItemsTableRow(BaseForItems):
    """
    CREATE TABLE items (
        id VARCHAR(255) PRIMARY KEY NOT NULL
        brand_name TEXT NOT NULL,
        name TEXT NOT NULL,
        price INT NOT NULL,
        images TEXT NOT NULL,
        gender VARCHAR NOT NULL,
        url TEXT NOT NULL,
        meta_keywords TEXT NOT NULL,
        meta_description TEXT NOT NULL,
        meta_content TEXT NOT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        deleted BOOL DEFAULT FALSE
        UNIQUE KEY (url)
    )
    """
    __tablename__ = "items"
    __table_args__ = ({"mysql_charset": "utf8mb4", "mysql_engine": "InnoDB"})

    id = Column(VARCHAR(255), primary_key=True, nullable=False)
    # brand_id = Column(VARCHAR(255), ForeignKey('brands.id', ondelete='CASCADE'), nullable=False)
    brand_name = Column(TEXT, nullable=False)
    name = Column(TEXT, nullable=False)
    price = Column(Integer, nullable=False)
    images = Column(TEXT, nullable=False)
    # gender_id = Column(Integer, ForeignKey('genders.id'), nullable=False)
    gender = Column(VARCHAR(50), nullable=False)
    url = Column(TEXT, nullable=False)
    meta_keywords = Column(TEXT, nullable=False)
    meta_description = Column(TEXT, nullable=False)
    meta_content = Column(TEXT, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
    deleted = Column(Boolean, default=False)

    def update(self, other: ItemsTableRow):
        self.brand_name = other.brand_name
        self.name = other.name
        self.price = other.price
        self.images = other.images
        self.gender = other.gender
        self.url = other.url
        self.meta_keywords = other.meta_keywords
        self.meta_description = other.meta_description
        self.meta_content = other.meta_content
