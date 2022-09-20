from typing import Optional, NoReturn

from injector import inject

from domain.model.category import CategoryId, Category, CategoryName
from domain.model.gender import Gender
from domain.model.query import QuerySet
from domain.model.url import URL
from port.adapter.persistence.repository.mysql.category.driver import CategoriesCrud, CategoriesTableRow, \
    CategoryQueriesTableRow, CategoryRelationsTableRow, CategoryQueriesCrud, CategoryRelationsCrud


class DriverManagerCategory:
    @inject
    def __init__(self,
                 categories_crud: CategoriesCrud,
                 category_queries_crud: CategoryQueriesCrud,
                 category_relations_crud: CategoryRelationsCrud):
        self.__categories_crud = categories_crud
        self.__category_queries_crud = category_queries_crud
        self.__category_relations_crud = category_relations_crud

    def find_by_id(self, category_id: CategoryId) -> Optional[Category]:
        categories_table_row = self.__categories_crud.find_by_id(category_id.value)
        category_queries_table_row = self.__category_queries_crud.find_by_category_id(category_id.value)
        category_relations_table_row_list = self.__category_relations_crud.find_by_parent_category_id(category_id.value)

        if categories_table_row is None or category_queries_table_row is None:
            return None
        return Category(
            CategoryId(categories_table_row.id),
            Gender[categories_table_row.gender],
            CategoryName(categories_table_row.name),
            URL(categories_table_row.image_url),
            [CategoryId(t.child_category_id) for t in category_relations_table_row_list],
            category_queries_table_row.to_query_set()
        )

    def upsert(self, category: Category) -> NoReturn:
        self.__categories_crud.upsert(CategoriesTableRow.of(category))
        self.__category_queries_crud.upsert(CategoryQueriesTableRow.of(category))
        self.__category_relations_crud.upsert(CategoryRelationsTableRow.of(category))

    def delete(self, category_id: CategoryId) -> NoReturn:
        self.__categories_crud.delete(category_id.value)
