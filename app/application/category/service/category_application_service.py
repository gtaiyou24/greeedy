from typing import NoReturn

from injector import singleton, inject

from application.category.dpo import GetCategoryTreeListDpo
from domain.model.category import CategoryRepository
from domain.model.gender import Gender


@singleton
class CategoryApplicationService:
    @inject
    def __init__(self, category_repository: CategoryRepository):
        self.__category_repository = category_repository

    def get_category_tree_list(self, a_gender: str) -> GetCategoryTreeListDpo:
        gender = Gender[a_gender]
        category_tree_list = self.__category_repository.category_tree(gender)
        return GetCategoryTreeListDpo(list=category_tree_list)

    def create(self, ) -> NoReturn:
        pass

    def update(self) -> NoReturn:
        pass
