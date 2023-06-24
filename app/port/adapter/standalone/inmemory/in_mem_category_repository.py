from typing import Optional, NoReturn

from slf4py import set_logger

from domain.model.category import CategoryRepository, CategoryTree, Category, CategoryId, CategoryName
from domain.model.gender import Gender
from domain.model.query import Operator, QuerySet, Query
from domain.model.url import URL


@set_logger
class InMemCategoryRepository(CategoryRepository):
    category_dict: dict[CategoryId:Category] = {}

    def __init__(self):
        self.save(Category(CategoryId('WOMEN'), Gender.WOMEN, CategoryName('レディース'),
                           URL('https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg'),
                           [CategoryId('women-tops'), CategoryId('women-outwear'), CategoryId('women-pants'),
                            CategoryId('women-skirt'), CategoryId('women-onepiece')],
                           QuerySet({})))
        self.save(Category(CategoryId('women-tops'), Gender.WOMEN, CategoryName('トップス'),
                           URL('https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg'),
                           [CategoryId('women-tops-1'), CategoryId('women-tops-2'), CategoryId('women-tops-3'),
                            CategoryId('women-tops-4'), CategoryId('women-tops-5'), CategoryId('women-tops-6'),
                            CategoryId('women-tops-7')], QuerySet({Operator.OR: [Query('トップス')]})))
        self.save(Category(CategoryId('women-tops-1'), Gender.WOMEN, CategoryName('Tシャツ/カットソー'),
                           URL('https://img.ltwebstatic.com/images3_pi/2021/11/25/163780557807890b150c834e0a64613c41cf312c01_thumbnail_600x.webp'),
                           [], QuerySet({Operator.OR: [Query('Tシャツ'), Query('カットソー')]})))
        self.save(Category(CategoryId('women-tops-2'), Gender.WOMEN, CategoryName('シャツ/ブラウス'),
                           URL('https://img.ltwebstatic.com/images3_pi/2021/07/08/162573610913a69d701058e5fc16b7a6c8036fbe29_thumbnail_600x.webp'),
                           [], QuerySet({Operator.OR: [Query('シャツ'), Query('ブラウス')]})))
        self.save(Category(CategoryId('women-tops-3'), Gender.WOMEN, CategoryName('ニット/セーター'),
                           URL('https://www.dzimg.com/Dahong/201911/860222_17428735_k3.jpg'), [],
                           QuerySet({Operator.OR: [Query('ニット'), Query('セーター')]})))
        self.save(Category(CategoryId('women-tops-4'), Gender.WOMEN, CategoryName('ベスト'),
                           URL('https://img.ltwebstatic.com/images3_pi/2021/06/23/16244509286debc49a0974a3f8dc9d441d43af3769_thumbnail_600x.webp'),
                           [], QuerySet({Operator.OR: [Query('ベスト')]})))
        self.save(Category(CategoryId('women-tops-5'), Gender.WOMEN, CategoryName('パーカー'),
                           URL('https://img.ltwebstatic.com/images3_pi/2021/08/03/1627980422b033c91e2fa51ba21a29517569abb6f4_thumbnail_600x.webp'),
                           [], QuerySet({Operator.OR: [Query('パーカー')]})))
        self.save(Category(CategoryId('women-tops-6'), Gender.WOMEN, CategoryName('スウェット'),
                           URL('https://www.dzimg.com/Dahong/202110/1230699_19451240_k3.jpg'), [],
                           QuerySet({Operator.OR: [Query('スウェット')]})))
        self.save(Category(CategoryId('women-tops-7'), Gender.WOMEN, CategoryName('カーディガン'),
                           URL('https://img.ltwebstatic.com/images3_pi/2020/08/14/1597381885c1f77b726f6f6b56ab72d6535c112f10_thumbnail_600x.webp'),
                           [],
                           QuerySet({Operator.OR: [Query('カーディガン')]})))
        self.save(Category(CategoryId('women-outwear'), Gender.WOMEN, CategoryName('ジャケット/アウター'),
                           URL('https://www.dzimg.com/Dahong/202109/1200225_19202545_k3.gif'),
                           [CategoryId('women-outwear-1'), CategoryId('women-outwear-2'), CategoryId('women-outwear-3'),
                            CategoryId('women-outwear-4'), CategoryId('women-outwear-5'), CategoryId('women-outwear-6'),
                            CategoryId('women-outwear-7'), CategoryId('women-outwear-8'), CategoryId('women-outwear-9'),
                            CategoryId('women-outwear-10')],
                           QuerySet({Operator.OR: [Query('ジャケット'), Query('アウター')]})))
        self.save(Category(CategoryId('women-outwear-1'), Gender.WOMEN, CategoryName('テーラードジャケット'),
                           URL('https://www.dzimg.com/Dahong/202109/1200225_19202545_k3.gif'), [],
                           QuerySet({Operator.OR: [Query('テーラードジャケット')]})))
        self.save(Category(CategoryId('women-outwear-2'), Gender.WOMEN, CategoryName('ノーカラージャケット'),
                           URL('https://www.dzimg.com/Dahong/202112/1280796_19825714_k3.jpg'), [],
                           QuerySet({Operator.OR: [Query('ノーカラージャケット')]})))
        self.save(Category(CategoryId('women-outwear-3'), Gender.WOMEN, CategoryName('ノーカラーコート'),
                           URL('https://www.dzimg.com/Dahong/202111/1258963_19613088_k3.jpg'), [],
                           QuerySet({Operator.OR: [Query('ノーカラーコート')]})))
        self.save(Category(CategoryId('women-outwear-4'), Gender.WOMEN, CategoryName('デニムジャケット'),
                           URL('https://cdn.grail.bz/images/goods/d/fo96l/fo96l_v1.jpg'), [],
                           QuerySet({Operator.OR: [Query('デニムジャケット')]})))
        self.save(Category(CategoryId('women-outwear-4'), Gender.WOMEN, CategoryName('デニムジャケット'),
                           URL('https://cdn.grail.bz/images/goods/d/fo96l/fo96l_v1.jpg'), [],
                           QuerySet({Operator.OR: [Query('デニムジャケット')]})))
        self.save(Category(CategoryId('women-outwear-5'), Gender.WOMEN, CategoryName('ライダースジャケット'),
                           URL('https://cdn.grail.bz/images/goods/d/iz112/iz112_v1.jpg'), [],
                           QuerySet({Operator.OR: [Query('ライダースジャケット')]})))
        self.save(Category(CategoryId('women-outwear-6'), Gender.WOMEN, CategoryName('ブルゾン'),
                           URL('https://cdn.grail.bz/images/goods/d/iz378/iz378_v1.jpg'), [],
                           QuerySet({Operator.OR: [Query('ブルゾン')]})))
        self.save(Category(CategoryId('women-outwear-7'), Gender.WOMEN, CategoryName('ミリタリージャケット'),
                           URL('https://www.dzimg.com/Dahong/201703/704505_16034539_k3_4.jpg'), [],
                           QuerySet({Operator.OR: [Query('ミリタリージャケット')]})))
        self.save(Category(CategoryId('women-outwear-8'), Gender.WOMEN, CategoryName('MA-1'),
                           URL('https://www.dzimg.com/Dahong/202111/1245560_19486927_k3.gif'), [],
                           QuerySet({Operator.OR: [Query('MA1')]})))
        self.save(Category(CategoryId('women-outwear-9'), Gender.WOMEN, CategoryName('トレンチコート'),
                           URL('https://www.dzimg.com/Dahong/202102/1050177_18538764_k3.jpg'), [],
                           QuerySet({Operator.OR: [Query('トレンチコート')]})))
        self.save(Category(CategoryId('women-outwear-10'), Gender.WOMEN, CategoryName('チェスターコート'),
                           URL('https://www.dzimg.com/Dahong/202010/984471_18113399_k3.gif'), [],
                           QuerySet({Operator.OR: [Query('チェスターコート')]})))
        self.save(Category(CategoryId('women-pants'), Gender.WOMEN, CategoryName('パンツ'),
                           URL('https://img.ltwebstatic.com/images3_pi/2021/09/18/163194975494872b1dbf205e2b799463819854c5e0.webp'),
                           [CategoryId('women-pants-1'), CategoryId('women-pants-2'),
                            CategoryId('women-pants-3'), CategoryId('women-pants-4')],
                           QuerySet({Operator.OR: [Query('パンツ')]})))
        self.save(Category(CategoryId('women-pants-1'), Gender.WOMEN, CategoryName('デニムパンツ'),
                           URL('https://cdn.grail.bz/images/goods/d/cu289/cu289_v1.jpg'), [],
                           QuerySet({Operator.OR: [Query('デニムパンツ')]})))
        self.save(Category(CategoryId('women-pants-2'), Gender.WOMEN, CategoryName('チノパン'),
                           URL('https://cdn.grail.bz/images/goods/d/k8706w/k8706w_v1.jpg'), [],
                           QuerySet({Operator.OR: [Query('チノパン')]})))
        self.save(Category(CategoryId('women-pants-3'), Gender.WOMEN, CategoryName('スラックス'),
                           URL('https://www.dzimg.com/Dahong/202110/1224795_19392681_k3.jpg'), [],
                           QuerySet({Operator.OR: [Query('スラックス')]})))
        self.save(Category(CategoryId('women-pants-4'), Gender.WOMEN, CategoryName('フレアパンツ'),
                           URL('https://cdn.grail.bz/images/goods/d/cu34/cu34_v1.jpg'), [],
                           QuerySet({Operator.OR: [Query('フレアパンツ')]})))
        self.save(Category(CategoryId('women-skirt'), Gender.WOMEN, CategoryName('スカート'),
                              URL('https://img.ltwebstatic.com/images3_pi/2021/07/17/1626515436968136d71b8dfc7aaf86c1e6f7a58a35_thumbnail_600x.webp'),
                              [CategoryId('women-skirt-1'), CategoryId('women-skirt-2'), CategoryId('women-skirt-3'),
                               CategoryId('women-skirt-4')], QuerySet({Operator.OR: [Query('スカート')]})))
        self.save(Category(CategoryId('women-skirt-1'), Gender.WOMEN, CategoryName('フレアスカート'),
                           URL('https://www.dzimg.com/Dahong/202201/1295073_20026004_k3.jpg'), [],
                           QuerySet({Operator.OR: [Query('フレアスカート')]})))
        self.save(Category(CategoryId('women-skirt-2'), Gender.WOMEN, CategoryName('マーメイドスカート'),
                           URL('https://cdn.grail.bz/images/goods/d/gc29/gc29_v1.jpg'), [],
                           QuerySet({Operator.OR: [Query('マーメイドスカート')]})))
        self.save(Category(CategoryId('women-skirt-3'), Gender.WOMEN, CategoryName('タイトスカート'),
                           URL('https://www.dzimg.com/Dahong/202111/1253205_19557262_k3.jpg'), [],
                           QuerySet({Operator.OR: [Query('タイトスカート')]})))
        self.save(Category(CategoryId('women-skirt-4'), Gender.WOMEN, CategoryName('ギャザースカート'),
                           URL('https://gd.image-qoo10.jp/%e3%82%b9%e3%82%ab%e3%83%bc%e3%83%88-%e3%82%ae%e3%83%a3%e3%82%b6%e3%83%bc-%e3%83%ad%e3%83%b3%e3%82%b0-%e3%83%9e%e3%82%ad%e3%82%b7%e4%b8%88-%e5%85%a84%e8%89%b2-%e9%9f%93%e5%9b%bd-30%e4%bb%a3-40%e4%bb%a3-50%e4%bb%a3-%e6%af%8d%e3%81%ae%e6%97%a5-%e3%82%bb%e3%83%bc%e3%83%ab-%e3%82%aa%e3%83%bc%e3%83%97%e3%83%b3%e8%a8%98%e5%bf%b5-2019%e5%b9%b4-%e6%98%a5/li/570/726/1208726570.g_400-w_g.jpg'),
                           [],
                           QuerySet({Operator.OR: [Query('ギャザースカート')]})))
        self.save(Category(CategoryId('women-onepiece'), Gender.WOMEN, CategoryName('ワンピース'),
                           URL('https://www.dzimg.com/Dahong/202109/1210043_19276844_k3.jpg'),
                           [CategoryId('women-onepiece-1'), CategoryId('women-onepiece-2'),
                            CategoryId('women-onepiece-3')],
                           QuerySet({Operator.OR: [Query('ワンピース')]})))
        self.save(Category(CategoryId('women-onepiece-1'), Gender.WOMEN, CategoryName('シャツワンピース'),
                           URL('https://www.dzimg.com/Dahong/202201/1309074_20046036_k3.jpg'), [],
                           QuerySet({Operator.OR: [Query('シャツワンピース')]})))
        self.save(Category(CategoryId('women-onepiece-2'), Gender.WOMEN, CategoryName('ジャンパースカート'),
                           URL('https://cdn.grail.bz/images/goods/d/rut747/rut747_v1.jpg'), [],
                           QuerySet({Operator.OR: [Query('ジャンパースカート'), Query('キャミソールワンピース')]})))
        self.save(Category(CategoryId('women-onepiece-3'), Gender.WOMEN, CategoryName('ニットワンピース'),
                           URL('https://cdn.grail.bz/images/goods/d/rut785/rut785_v1.jpg'), [],
                           QuerySet({Operator.OR: [Query('ニットワンピース')]})))

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
