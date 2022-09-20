from typing import NoReturn, Optional

from injector import inject

from config import MySQLConfig
from config.db import session
from port.adapter.persistence.repository.mysql.category.driver import CategoryQueriesTableRow


class CategoryQueriesCrud:
    def __init__(self):
        self.__session = session

    def upsert(self, category_queries_table_row: CategoryQueriesTableRow) -> NoReturn:
        if category_queries_table_row.id is None:
            self.__session.add(category_queries_table_row)
            return

        optional = self.__session.query(CategoryQueriesTableRow).get(category_queries_table_row.id)
        if optional is None:
            self.__session.add(category_queries_table_row)
        else:
            optional.update(category_queries_table_row)

    def find_by_category_id(self, category_id: str) -> Optional[CategoryQueriesTableRow]:
        return self.__session.query(CategoryQueriesTableRow)\
            .filter(CategoryQueriesTableRow.category_id == category_id)\
            .first()
