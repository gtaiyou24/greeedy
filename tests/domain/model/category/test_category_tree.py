from typing import NoReturn

import pytest

from domain.model.category import CategoryTree, CategoryId


class TestCategoryTree:
    class Test_生成について:
        def test_親カテゴリIDと子カテゴリツリーのリスト指定で生成できる(self) -> NoReturn:
            try:
                CategoryTree(CategoryId('WOMEN'), [
                    CategoryTree(CategoryId('women-tops'), [
                        CategoryTree(CategoryId('women-tops-t_shirt'), []),
                        CategoryTree(CategoryId('women-tops-sweater'), [])
                    ]),
                    CategoryTree(CategoryId('women-pants'), [])
                ])
            except Exception:
                pytest.fail('This code should be executed.')

    class Test_hasメソッドについて:
        def test_カテゴリID指定でカテゴリーツリー内に該当カテゴリIDが存在する場合はTrueを返す(self) -> NoReturn:
            category_tree = CategoryTree(CategoryId('WOMEN'), [
                CategoryTree(CategoryId('women-tops'), [
                    CategoryTree(CategoryId('women-tops-t_shirt'), []),
                    CategoryTree(CategoryId('women-tops-sweater'), [])
                ]),
                CategoryTree(CategoryId('women-pants'), [])
            ])

            assert category_tree.has(CategoryId('women-tops-t_shirt'))

        def test_該当カテゴリIDが存在しない場合はFalseを返す(self) -> NoReturn:
            category_tree = CategoryTree(CategoryId('WOMEN'), [
                CategoryTree(CategoryId('women-tops'), [
                    CategoryTree(CategoryId('women-tops-t_shirt'), []),
                    CategoryTree(CategoryId('women-tops-sweater'), [])
                ]),
                CategoryTree(CategoryId('women-pants'), [])
            ])

            assert not category_tree.has(CategoryId('men-tops-t_shirt'))

    class Test_all_category_idsメソッドについて:
        def test_カテゴリツリー内の全てのカテゴリIDを取得できる(self) -> NoReturn:
            category_tree = CategoryTree(CategoryId('WOMEN'), [
                CategoryTree(CategoryId('women-tops'), [
                    CategoryTree(CategoryId('women-tops-t_shirt'), []),
                    CategoryTree(CategoryId('women-tops-sweater'), [])
                ]),
                CategoryTree(CategoryId('women-pants'), [])
            ])

            assert category_tree.all_category_ids() == {
                CategoryId('WOMEN'), CategoryId('women-tops'), CategoryId('women-tops-t_shirt'),
                CategoryId('women-tops-sweater'), CategoryId('women-pants')
            }
