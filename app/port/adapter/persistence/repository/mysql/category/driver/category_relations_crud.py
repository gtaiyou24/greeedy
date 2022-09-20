from typing import NoReturn, List

from injector import inject

from config import MySQLConfig
from config.db import session
from port.adapter.persistence.repository.mysql.category.driver import CategoryRelationsTableRow


class CategoryRelationsCrud:
    def __init__(self):
        self.__session = session

    def upsert(self, category_relations_table_row_list: List[CategoryRelationsTableRow]) -> NoReturn:
        parent_category_ids = set([t.parent_category_id for t in category_relations_table_row_list])

        self.__session.query(CategoryRelationsTableRow)\
            .filter(CategoryRelationsTableRow.parent_category_id.in_(parent_category_ids))\
            .delete()

        for t in category_relations_table_row_list:
            self.__session.add(t)

    def find_by_parent_category_id(self, parent_category_id: str) -> List[CategoryRelationsTableRow]:
        return self.__session.query(CategoryRelationsTableRow)\
            .filter(CategoryRelationsTableRow.parent_category_id == parent_category_id)\
            .all()
