from typing import Optional, NoReturn

from injector import inject
from sqlalchemy.orm import Session

from port.adapter.persistence.repository.mysql.category.driver import CategoriesTableRow


class CategoriesCrud:
    @inject
    def __init__(self, session: Session):
        self.__session = session

    def find_by_id(self, id: str) -> Optional[CategoriesTableRow]:
        categories_table_row = self.__session.query(CategoriesTableRow).get(id)
        return categories_table_row

    def upsert(self, categories_table_row: CategoriesTableRow) -> NoReturn:
        optional = self.find_by_id(categories_table_row.id)
        if optional is None:
            self.__session.add(categories_table_row)
        else:
            optional.update(categories_table_row)

    def delete(self, id: str) -> NoReturn:
        self.__session.query(CategoriesTableRow)\
            .filter(CategoriesTableRow.id == id)\
            .delete()
