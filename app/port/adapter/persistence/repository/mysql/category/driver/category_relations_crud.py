from typing import NoReturn, List

from injector import inject

from config import MySQLConfig
from port.adapter.persistence.repository.mysql.category.driver import BaseForCategoryRelations, \
    CategoryRelationsTableRow


class CategoryRelationsCrud:

    @inject
    def __init__(self, mysql_config: MySQLConfig):
        self.__session = mysql_config.session()
        BaseForCategoryRelations.metadata.create_all(bind=mysql_config.engine())

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
