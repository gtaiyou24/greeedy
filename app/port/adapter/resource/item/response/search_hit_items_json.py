from __future__ import annotations

from typing import List, Set

from pydantic import BaseModel, Field

from application.item.dpo import SearchHitItemsDpo


class SearchHitItemsJson(BaseModel):
    """アイテム検索結果を返すクラス"""

    class Request(BaseModel):
        keyword: str = Field(description="キーワード")
        category: str = Field(description="カテゴリ名")
        colors: Set[str] = Field(description="カラー一覧")
        styles: Set[str] = Field(description="系統一覧")
        price_from: int = Field(description="価格下限")
        price_to: int = Field(description="価格上限")
        sort: str = Field(description="並び順")

    class Hit(BaseModel):
        class Image(BaseModel):
            type: str = Field(default="MODEL_WEARING", title="画像種別", description="MODEL_WEARING=モデル着用画像")
            color: str = Field(default="White", title="カラー")
            url: str = Field(title="画像URL")

        ranking: int = Field(description="検索結果の順位")
        id: str = Field(description="アイテムID")
        name: str = Field(description="アイテム名")
        brand_name: str = Field(description="ブランド名")
        price: int = Field(description="価格")
        gender: str = Field(title="性別")
        images: List[Hit.Image] = Field(description="画像URL一覧")
        page_url: str = Field(description="アイテムのページURL")

    total_results_available: int = Field(description="総検索ヒット件数")
    total_results_returned: int = Field(description="返却された商品件数")
    first_results_position: int = Field(description="最初のデータが何件目にあたるか(最初=1)")
    # request: SearchHitItemsJson.Request = Field(description="リクエストされたデータ")
    hits: List[SearchHitItemsJson.Hit] = Field(description="検索にヒットした商品一覧")

    @staticmethod
    def make_by(search_hit_items_dpo: SearchHitItemsDpo, start: int) -> SearchHitItemsJson:
        hits = []
        for i, item in enumerate(search_hit_items_dpo.list):
            ranking = start + i
            hit = SearchHitItemsJson.Hit(ranking=ranking, id=item.id.value, name=item.name.text,
                                         brand_name=item.brand_name.text, price=item.price.amount,
                                         gender=item.gender.name,
                                         images=[
                                             SearchHitItemsJson.Hit.Image(
                                                 type=image.type.name,
                                                 color=image.color.name,
                                                 url=image.url.address
                                             ) for image in item.images.list
                                         ],
                                         page_url=item.page.url.address)
            hits.append(hit)

        first_results_position = start
        if len(hits) == 0:
            first_results_position = 0

        return SearchHitItemsJson(
            total_results_available=search_hit_items_dpo.total_results_available,
            total_results_returned=len(search_hit_items_dpo.list),
            first_results_position=first_results_position,
            hits=hits
        )
