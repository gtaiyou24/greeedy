from typing import NoReturn, Optional

from injector import inject
from sqlalchemy.orm import Session

from port.adapter.persistence.repository.mysql.category.driver import CategoryQueriesTableRow


class CategoryQueriesCrud:
    @inject
    def __init__(self, session: Session):
        self.__session = session

    def upsert(self, category_queries_table_row: CategoryQueriesTableRow) -> NoReturn:
        optional = self.find_by_category_id(category_queries_table_row.category_id)
        if optional is None:
            self.__session.add(category_queries_table_row)
        else:
            optional.update(category_queries_table_row)

    def find_by_category_id(self, category_id: str) -> Optional[CategoryQueriesTableRow]:
        return self.__session.query(CategoryQueriesTableRow)\
            .filter(CategoryQueriesTableRow.category_id == category_id)\
            .first()
