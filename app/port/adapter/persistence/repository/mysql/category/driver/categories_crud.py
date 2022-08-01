from typing import Optional, NoReturn

from injector import inject
from sqlalchemy.orm import Session

from config import MySQLConfig
from port.adapter.persistence.repository.mysql.category.driver import BaseForCategories, CategoriesTableRow


class CategoriesCrud:
    @inject
    def __init__(self, config: MySQLConfig):
        self.__engine = config.engine()
        self.__session = config.session()
        BaseForCategories.metadata.create_all(bind=self.__engine)

    def find_by_id(self, id: str) -> Optional[CategoriesTableRow]:
        with Session(self.__engine, future=True) as session:
            categories_table_row = session.query(CategoriesTableRow).get(id)
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
