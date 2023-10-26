from pathlib import Path
from typing import Optional, NoReturn

import yaml
from slf4py import set_logger

from domain.model.category import CategoryRepository, CategoryTree, Category, CategoryId, CategoryName
from domain.model.gender import Gender
from domain.model.query import Operator, QuerySet, Query
from domain.model.url import URL


@set_logger
class InMemCategoryRepository(CategoryRepository):
    category_dict: dict[CategoryId:Category] = {}

    def __init__(self):
        # load config file
        with open(Path(__file__).parent / "category.yaml", "r") as f:
            categories = yaml.load(f, Loader=yaml.FullLoader)
        for category in categories:
            query_set = category.get('query_set') if category.get('query_set') else {}
            sub_category_ids = category.get('sub_category_ids') if category.get('sub_category_ids') else []

            all = {}
            for o, queries in query_set.items():
                all[Operator.value_of(o)] = [Query(q['text'], Operator.value_of(q['operator'])) for q in queries]

            a_category = Category(
                CategoryId(category['category_id']),
                Gender[category['gender']],
                CategoryName(category['name']),
                URL(category['url']),
                [CategoryId(sub_category_id) for sub_category_id in sub_category_ids],
                QuerySet(all)
            )
            self.save(a_category)

        self.save(Category(CategoryId('WOMEN'), Gender.WOMEN, CategoryName('レディース'),
                           URL('https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg'),
                           [CategoryId('women-tops'), CategoryId('women-outwear'), CategoryId('women-pants'),
                            CategoryId('women-skirt'), CategoryId('women-onepiece')],
                           QuerySet({})))

    def category_tree_of(self, category_id: CategoryId) -> CategoryTree:
        root_category = self.category_dict.get(category_id)

        children = list()
        for category_id in root_category.sub_category_ids:
            child_category_tree = self.category_tree_of(category_id)
            children.append(child_category_tree)
        return CategoryTree(root_category.id, children)

    def categories_of(self, category_ids: set[CategoryId]) -> set[Category]:
        categories = set()
        for id in category_ids:
            category = self.category_dict.get(id, None)
            if category is None:
                continue
            categories.add(category)
        return categories

    def category_list_of(self, start: int, limit: int, sort: str) -> list[Category]:
        i = start - 1
        return list(self.category_dict.values())[i:i+limit]

    def category_of(self, category_id: CategoryId) -> Optional[Category]:
        return self.category_dict.get(category_id, None)

    def save(self, category: Category) -> NoReturn:
        self.category_dict[category.id] = category

    def delete(self, category_id: CategoryId) -> NoReturn:
        self.category_dict.pop(category_id)
