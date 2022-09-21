from typing import NoReturn

from injector import singleton, inject

from application import ApplicationServiceLifeCycle
from application.category.command import SaveCategoryCommand
from application.category.dpo import GetCategoryTreeListDpo, GetCategoryDpo
from domain.model.category import CategoryRepository, CategoryId, Category, CategoryName
from domain.model.gender import Gender
from domain.model.query import QuerySet, Operator, Query
from domain.model.url import URL
from exception import SystemException, ErrorCode


@singleton
class CategoryApplicationService:
    @inject
    def __init__(self,
                 application_service_life_cycle: ApplicationServiceLifeCycle,
                 category_repository: CategoryRepository):
        self.__application_service_life_cycle = application_service_life_cycle
        self.__category_repository = category_repository

    def get_category_tree_list(self, a_gender: str) -> GetCategoryTreeListDpo:
        gender = Gender[a_gender]
        category_tree_list = self.__category_repository.category_tree(gender)
        return GetCategoryTreeListDpo(list=category_tree_list)

    def get(self, a_category_id: str) -> GetCategoryDpo:
        category_id = CategoryId(a_category_id)
        category = self.__category_repository.category_of(category_id)

        if category is None:
            raise SystemException(
                ErrorCode.CATEGORY_NOT_FOUND, 'カテゴリID {} のカテゴリが見つかりませんでした'.format(category_id.value))

        return GetCategoryDpo(category=category)

    def save(self, command: SaveCategoryCommand) -> NoReturn:
        sub_category_ids = [CategoryId(sub_category_id) for sub_category_id in command.sub_category_ids]

        _all = {}
        for operator, queries in command.operator_and_queries.items():
            _all[Operator.value_of(operator)] = {Query(query.text, Operator.value_of(query.operator)) for query in queries}

        category = Category(CategoryId(command.id), Gender[command.gender], CategoryName(command.name),
                            URL(command.image_url), sub_category_ids, QuerySet(_all))

        try:
            self.__application_service_life_cycle.begin(False)
            self.__category_repository.save(category)
            self.__application_service_life_cycle.success()
        except Exception as e:
            self.__application_service_life_cycle.fail(e)

    def delete(self, a_category_id: str) -> NoReturn:
        category_id = CategoryId(a_category_id)
        try:
            self.__application_service_life_cycle.begin()
            self.__category_repository.delete(category_id)
        except Exception as e:
            self.__application_service_life_cycle.fail(e)
        else:
            self.__application_service_life_cycle.success()
