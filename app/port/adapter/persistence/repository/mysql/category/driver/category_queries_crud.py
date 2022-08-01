from typing import NoReturn, Optional

from injector import inject

from config import MySQLConfig
from port.adapter.persistence.repository.mysql.category.driver import CategoryQueriesTableRow, BaseForCategoryQueries


class CategoryQueriesCrud:
    @inject
    def __init__(self, config: MySQLConfig):
        self.__engine = config.engine()
        self.__session = config.session()
        BaseForCategoryQueries.metadata.create_all(bind=self.__engine)

    def upsert(self, category_queries_table_row: CategoryQueriesTableRow) -> NoReturn:
        optional = self.__session.query(CategoryQueriesTableRow).get(category_queries_table_row.id)
        if optional is None:
            self.__session.add(category_queries_table_row)
        else:
            optional.update(category_queries_table_row)

    def find_by_category_id(self, category_id: str) -> Optional[CategoryQueriesTableRow]:
        return self.__session.query(CategoryQueriesTableRow)\
            .filter(CategoryQueriesTableRow.category_id == category_id)\
            .first()