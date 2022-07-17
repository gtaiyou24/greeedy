from typing import Optional, List

from injector import inject
from sqlalchemy import select
from sqlalchemy.orm import Session

from config import MySQLConfig
from port.adapter.persistence.repository.mysql.item.driver import BaseForItems, ItemsTableRow


class ItemsCrud:
    @inject
    def __init__(self, config: MySQLConfig):
        self.__engine = config.engine()
        BaseForItems.metadata.create_all(bind=self.__engine)  # itemsテーブル作成

    def find_by_id(self, id: str) -> Optional[ItemsTableRow]:
        with Session(self.__engine, future=True) as session:
            items_table_row: ItemsTableRow = session.query(ItemsTableRow).get(id)
            return items_table_row

    def find_all_by_ids(self, ids: List[str]) -> List[ItemsTableRow]:
        with Session(self.__engine, future=True) as session:
            stmt = select(ItemsTableRow).where(ItemsTableRow.id.in_(ids))
            return list(session.execute(stmt).all())

    def upsert(self, item_table_row: ItemsTableRow):
        optional = self.find_by_id(item_table_row.id)
        with Session(self.__engine, future=True) as session:
            if optional is None:
                session.add(item_table_row)
            else:
                optional.update(item_table_row)
            session.commit()

    def delete(self, id: str):
        with Session(self.__engine, future=True) as session:
            items_table_row: ItemsTableRow = session.query(ItemsTableRow).get(id)
            items_table_row.deleted = True
            session.commit()
