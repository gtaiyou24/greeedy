from injector import inject

from domain.model.category import CategoryTree, CategoryId
from port.adapter.persistence.repository.mysql.category.driver import CategoryRelationsCrud


class DriverManagerCategoryTree:
    @inject
    def __init__(self,
                 category_relations_crud: CategoryRelationsCrud):
        self.__category_relations_crud = category_relations_crud

    def find_by_category_id(self, category_id: CategoryId) -> CategoryTree:
        category_relation_table_row_list = self.__category_relations_crud.find_by_parent_category_id(category_id.value)

        children = list()
        for tr in category_relation_table_row_list:
            child_category_id = CategoryId(tr.child_category_id)
            child_category_tree = self.find_by_category_id(child_category_id)
            children.append(child_category_tree)
        return CategoryTree(category_id, children)
