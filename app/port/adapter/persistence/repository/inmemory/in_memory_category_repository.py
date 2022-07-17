from typing import List, Optional

from domain.model.category import CategoryRepository, Category, CategoryId, CategoryName, CategoryTree
from domain.model.gender import Gender
from domain.model.query import QuerySet, Operator, Query
from domain.model.url import URL


WOMEN_トップス = Category(CategoryId("women-tops"), Gender.WOMEN, CategoryName("トップス"),
                      URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"),
                      [CategoryId("women-tops-1"), CategoryId("women-tops-2"), CategoryId("women-tops-3"),
                       CategoryId("women-tops-4"), CategoryId("women-tops-5"), CategoryId("women-tops-6"),
                       CategoryId("women-tops-7")],
                      QuerySet({Operator.OR: [Query("トップス")]}))
WOMEN_Tシャツ = Category(CategoryId("women-tops-1"), Gender.WOMEN, CategoryName("Tシャツ/カットソー"),
                      URL("https://img.ltwebstatic.com/images3_pi/2021/11/25/163780557807890b150c834e0a64613c41cf312c01_thumbnail_600x.webp"), [],
                      QuerySet({Operator.OR: [Query("Tシャツ"), Query("カットソー")]}))
WOMEN_シャツブラウス = Category(CategoryId("women-tops-2"), Gender.WOMEN, CategoryName("シャツ/ブラウス"),
                         URL("https://img.ltwebstatic.com/images3_pi/2021/07/08/162573610913a69d701058e5fc16b7a6c8036fbe29_thumbnail_600x.webp"), [],
                         QuerySet({Operator.OR: [Query("シャツ"), Query("ブラウス")]}))
WOMEN_ニットセーター = Category(CategoryId("women-tops-3"), Gender.WOMEN, CategoryName("ニット/セーター"),
                         URL("https://www.dzimg.com/Dahong/201911/860222_17428735_k3.jpg"), [],
                         QuerySet({Operator.OR: [Query("シャツ"), Query("ブラウス")]}))
WOMEN_ベスト = Category(CategoryId("women-tops-4"), Gender.WOMEN, CategoryName("ベスト"),
                     URL("https://img.ltwebstatic.com/images3_pi/2021/06/23/16244509286debc49a0974a3f8dc9d441d43af3769_thumbnail_600x.webp"), [],
                     QuerySet({Operator.OR: [Query("ベスト")]}))
WOMEN_パーカー = Category(CategoryId("women-tops-5"), Gender.WOMEN, CategoryName("パーカー"),
                      URL("https://img.ltwebstatic.com/images3_pi/2021/08/03/1627980422b033c91e2fa51ba21a29517569abb6f4_thumbnail_600x.webp"), [],
                      QuerySet({Operator.OR: [Query("パーカー")]}))
WOMEN_スウェット = Category(CategoryId("women-tops-6"), Gender.WOMEN, CategoryName("スウェット"),
                       URL("https://www.dzimg.com/Dahong/202110/1230699_19451240_k3.jpg"), [],
                       QuerySet({Operator.OR: [Query("スウェット")]}))
WOMEN_カーディガン = Category(CategoryId("women-tops-7"), Gender.WOMEN, CategoryName("カーディガン"),
                        URL("https://img.ltwebstatic.com/images3_pi/2020/08/14/1597381885c1f77b726f6f6b56ab72d6535c112f10_thumbnail_600x.webp"), [],
                        QuerySet({Operator.OR: [Query("カーディガン")]}))

WOMEN_ジャケットアウター = Category(CategoryId("women-outwear"), Gender.WOMEN, CategoryName("ジャケット/アウター"),
                           URL("https://www.dzimg.com/Dahong/202109/1200225_19202545_k3.gif"),
                           [CategoryId("women-outwear-1"), CategoryId("women-outwear-2"), CategoryId("women-outwear-3"),
                            CategoryId("women-outwear-4"), CategoryId("women-outwear-5"), CategoryId("women-outwear-6"),
                            CategoryId("women-outwear-7"), CategoryId("women-outwear-8"), CategoryId("women-outwear-9"),
                            CategoryId("women-outwear-10")],
                           QuerySet({Operator.OR: [Query("ジャケット"), Query("アウター")]}))
WOMEN_テーラードジャケット = Category(CategoryId("women-outwear-1"), Gender.WOMEN, CategoryName("テーラードジャケット"),
                            URL("https://www.dzimg.com/Dahong/202109/1200225_19202545_k3.gif"), [],
                            QuerySet({Operator.OR: [Query("テーラードジャケット")]}))
WOMEN_ノーカラージャケット = Category(CategoryId("women-outwear-2"), Gender.WOMEN, CategoryName("ノーカラージャケット"),
                            URL("https://www.dzimg.com/Dahong/202112/1280796_19825714_k3.jpg"), [],
                            QuerySet({Operator.OR: [Query("ノーカラージャケット")]}))
WOMEN_ノーカラーコート = Category(CategoryId("women-outwear-3"), Gender.WOMEN, CategoryName("ノーカラーコート"),
                          URL("https://www.dzimg.com/Dahong/202111/1258963_19613088_k3.jpg"), [],
                          QuerySet({Operator.OR: [Query("ノーカラーコート")]}))
WOMEN_デニムジャケット = Category(CategoryId("women-outwear-4"), Gender.WOMEN, CategoryName("デニムジャケット"),
                          URL("https://cdn.grail.bz/images/goods/d/fo96l/fo96l_v1.jpg"), [],
                          QuerySet({Operator.OR: [Query("デニムジャケット")]}))
WOMEN_ライダースジャケット = Category(CategoryId("women-outwear-5"), Gender.WOMEN, CategoryName("ライダースジャケット"),
                            URL("https://cdn.grail.bz/images/goods/d/iz112/iz112_v1.jpg"), [],
                            QuerySet({Operator.OR: [Query("ライダースジャケット")]}))
WOMEN_ブルゾン = Category(CategoryId("women-outwear-6"), Gender.WOMEN, CategoryName("ブルゾン"),
                      URL("https://cdn.grail.bz/images/goods/d/iz378/iz378_v1.jpg"), [],
                      QuerySet({Operator.OR: [Query("ブルゾン")]}))
WOMEN_ミリタリージャケット = Category(CategoryId("women-outwear-7"), Gender.WOMEN, CategoryName("ミリタリージャケット"),
                            URL("https://www.dzimg.com/Dahong/201703/704505_16034539_k3_4.jpg"), [],
                            QuerySet({Operator.OR: [Query("ミリタリージャケット")]}))
WOMEN_MA1 = Category(CategoryId("women-outwear-8"), Gender.WOMEN, CategoryName("MA-1"),
                     URL("https://www.dzimg.com/Dahong/202111/1245560_19486927_k3.gif"), [],
                     QuerySet({Operator.OR: [Query("MA1")]}))
WOMEN_トレンチコート = Category(CategoryId("women-outwear-9"), Gender.WOMEN, CategoryName("トレンチコート"),
                         URL("https://www.dzimg.com/Dahong/202102/1050177_18538764_k3.jpg"), [],
                         QuerySet({Operator.OR: [Query("トレンチコート")]}))
WOMEN_チェスターコート = Category(CategoryId("women-outwear-10"), Gender.WOMEN, CategoryName("チェスターコート"),
                          URL("https://www.dzimg.com/Dahong/202010/984471_18113399_k3.gif"), [],
                          QuerySet({Operator.OR: [Query("チェスターコート")]}))

WOMEN_デニムパンツ = Category(CategoryId("women-pants-1"), Gender.WOMEN, CategoryName("デニムパンツ"),
                        URL("https://cdn.grail.bz/images/goods/d/cu289/cu289_v1.jpg"), [],
                        QuerySet({Operator.OR: [Query("デニムパンツ")]}))
WOMEN_チノパン = Category(CategoryId("women-pants-2"), Gender.WOMEN, CategoryName("チノパン"),
                        URL("https://cdn.grail.bz/images/goods/d/k8706w/k8706w_v1.jpg"), [],
                        QuerySet({Operator.OR: [Query("チノパン")]}))
WOMEN_スラックス = Category(CategoryId("women-pants-3"), Gender.WOMEN, CategoryName("スラックス"),
                        URL("https://www.dzimg.com/Dahong/202110/1224795_19392681_k3.jpg"), [],
                        QuerySet({Operator.OR: [Query("スラックス")]}))
WOMEN_フレアパンツ = Category(CategoryId("women-pants-4"), Gender.WOMEN, CategoryName("フレアパンツ"),
                        URL("https://cdn.grail.bz/images/goods/d/cu34/cu34_v1.jpg"), [],
                        QuerySet({Operator.OR: [Query("フレアパンツ")]}))
WOMEN_パンツ = Category(CategoryId("women-pants"), Gender.WOMEN, CategoryName("パンツ"),
                     URL("https://img.ltwebstatic.com/images3_pi/2021/09/18/163194975494872b1dbf205e2b799463819854c5e0.webp"),
                     [WOMEN_デニムパンツ.id, WOMEN_チノパン.id, WOMEN_スラックス.id, WOMEN_フレアパンツ.id],
                     QuerySet({Operator.OR: [Query("パンツ")]}))

WOMEN_フレアスカート = Category(CategoryId("women-skirt-1"), Gender.WOMEN, CategoryName("フレアスカート"),
                         URL("https://www.dzimg.com/Dahong/202201/1295073_20026004_k3.jpg"), [],
                         QuerySet({Operator.OR: [Query("フレアスカート")]}))
WOMEN_マーメイドスカート = Category(CategoryId("women-skirt-2"), Gender.WOMEN, CategoryName("マーメイドスカート"),
                           URL("https://cdn.grail.bz/images/goods/d/gc29/gc29_v1.jpg"), [],
                           QuerySet({Operator.OR: [Query("マーメイドスカート")]}))
WOMEN_タイトスカート = Category(CategoryId("women-skirt-3"), Gender.WOMEN, CategoryName("タイトスカート"),
                           URL("https://www.dzimg.com/Dahong/202111/1253205_19557262_k3.jpg"), [],
                           QuerySet({Operator.OR: [Query("タイトスカート")]}))
WOMEN_ギャザースカート = Category(CategoryId("women-skirt-4"), Gender.WOMEN, CategoryName("ギャザースカート"),
                           URL("https://gd.image-qoo10.jp/%e3%82%b9%e3%82%ab%e3%83%bc%e3%83%88-%e3%82%ae%e3%83%a3%e3%82%b6%e3%83%bc-%e3%83%ad%e3%83%b3%e3%82%b0-%e3%83%9e%e3%82%ad%e3%82%b7%e4%b8%88-%e5%85%a84%e8%89%b2-%e9%9f%93%e5%9b%bd-30%e4%bb%a3-40%e4%bb%a3-50%e4%bb%a3-%e6%af%8d%e3%81%ae%e6%97%a5-%e3%82%bb%e3%83%bc%e3%83%ab-%e3%82%aa%e3%83%bc%e3%83%97%e3%83%b3%e8%a8%98%e5%bf%b5-2019%e5%b9%b4-%e6%98%a5/li/570/726/1208726570.g_400-w_g.jpg"), [],
                           QuerySet({Operator.OR: [Query("ギャザースカート")]}))
WOMEN_スカート = Category(CategoryId("women-skirt"), Gender.WOMEN, CategoryName("スカート"),
                      URL("https://img.ltwebstatic.com/images3_pi/2021/07/17/1626515436968136d71b8dfc7aaf86c1e6f7a58a35_thumbnail_600x.webp"),
                      [WOMEN_フレアスカート.id, WOMEN_マーメイドスカート.id, WOMEN_タイトスカート.id, WOMEN_ギャザースカート.id],
                      QuerySet({Operator.OR: [Query("スカート")]}))

WOMEN_シャツワンピース = Category(CategoryId("women-onepiece-1"), Gender.WOMEN, CategoryName("シャツワンピース"),
                          URL("https://www.dzimg.com/Dahong/202201/1309074_20046036_k3.jpg"), [],
                          QuerySet({Operator.OR: [Query("シャツワンピース")]}))
WOMEN_ジャンパースカート = Category(CategoryId("women-onepiece-2"), Gender.WOMEN, CategoryName("ジャンパースカート"),
                           URL("https://cdn.grail.bz/images/goods/d/rut747/rut747_v1.jpg"), [],
                           QuerySet({Operator.OR: [Query("ジャンパースカート"), Query("キャミソールワンピース")]}))
WOMEN_ニットワンピース = Category(CategoryId("women-onepiece-3"), Gender.WOMEN, CategoryName("ニットワンピース"),
                           URL("https://cdn.grail.bz/images/goods/d/rut785/rut785_v1.jpg"), [],
                           QuerySet({Operator.OR: [Query("ニットワンピース")]}))
WOMEN_ワンピース = Category(CategoryId("women-onepiece"), Gender.WOMEN, CategoryName("ワンピース"),
                       URL("https://www.dzimg.com/Dahong/202109/1210043_19276844_k3.jpg"),
                       [WOMEN_シャツワンピース.id, WOMEN_ジャンパースカート.id, WOMEN_ニットワンピース.id],
                       QuerySet({Operator.OR: [Query("ワンピース")]}))


class InMemCategoryRepository(CategoryRepository):
    __women_category_tree: List[CategoryTree] = [
        CategoryTree(WOMEN_トップス, [
            CategoryTree(WOMEN_Tシャツ, []),
            CategoryTree(WOMEN_シャツブラウス, []),
            CategoryTree(WOMEN_ベスト, []),
            CategoryTree(WOMEN_パーカー, []),
            CategoryTree(WOMEN_スウェット, []),
            CategoryTree(WOMEN_カーディガン, [])
        ]),
        CategoryTree(WOMEN_ジャケットアウター, [
            CategoryTree(WOMEN_テーラードジャケット, []),
            CategoryTree(WOMEN_ノーカラージャケット, []),
            CategoryTree(WOMEN_ノーカラーコート, []),
            CategoryTree(WOMEN_デニムジャケット, []),
            CategoryTree(WOMEN_ライダースジャケット, []),
            CategoryTree(WOMEN_ブルゾン, []),
            CategoryTree(WOMEN_ミリタリージャケット, []),
            CategoryTree(WOMEN_MA1, []),
            CategoryTree(WOMEN_トレンチコート, []),
            CategoryTree(WOMEN_チェスターコート, [])
        ]),
        CategoryTree(WOMEN_パンツ, [
            CategoryTree(WOMEN_デニムパンツ, []),
            CategoryTree(WOMEN_チノパン, []),
            CategoryTree(WOMEN_スラックス, []),
            CategoryTree(WOMEN_フレアパンツ, [])
        ]),
        CategoryTree(WOMEN_スカート, [
            CategoryTree(WOMEN_フレアスカート, []),
            CategoryTree(WOMEN_マーメイドスカート, []),
            CategoryTree(WOMEN_タイトスカート, []),
            CategoryTree(WOMEN_ギャザースカート, [])
        ]),
        CategoryTree(WOMEN_ワンピース, [
            CategoryTree(WOMEN_シャツワンピース, []),
            CategoryTree(WOMEN_ジャンパースカート, []),
            CategoryTree(WOMEN_ニットワンピース, [])
        ])
    ]

    __men_category_tree: List[CategoryTree] = [
        CategoryTree(
            Category(CategoryId("men-all"), Gender.MEN, CategoryName("すべてのアイテム"),
                     URL("https://daikore.com/wp-content/uploads/2021/03/d4.jpg"), [],
                     QuerySet({Operator.OR: []})),
            [])
    ]

    def category_tree(self, gender: Gender) -> List[CategoryTree]:
        if gender == Gender.WOMEN:
            return self.__women_category_tree
        elif gender == Gender.MEN:
            return self.__men_category_tree
        else:
            return []

    def category_of(self, category_id: CategoryId) -> Optional[Category]:
        all_category_tree = self.__women_category_tree + self.__men_category_tree
        for a_category_tree in all_category_tree:
            optional_category = a_category_tree.category_of(category_id)
            if optional_category is not None:
                return optional_category
        return None
