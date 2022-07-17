from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from application.item.dpo import GetItemListDpo


class GetItemListJson(BaseModel):
    class Item(BaseModel):
        id: str = Field(title="アイテムID")
        name: str = Field(title="アイテム名")
        brand_name: str = Field(title="ブランド名")
        price: int = Field(title="価格")
        description: str = Field(title="アイテム説明")
        gender: str = Field(title="性別")
        images: List[str] = Field(default=[], title="画像URL一覧")
        page_url: str = Field(title="アイテムのページURL")

    items: List[GetItemListJson.Item] = Field(title="アイテム一覧")

    @staticmethod
    def make_by(dpo: GetItemListDpo) -> GetItemListJson:
        return GetItemListJson(
            items=[GetItemListJson.Item(id=item.id.value,
                                        name=item.name.text,
                                        brand_name=item.brand_name.text,
                                        price=item.price.amount,
                                        description=item.description.text,
                                        gender=item.gender.name,
                                        images=[image.url.address for image in item.images.list],
                                        page_url=item.url.address) for item in dpo.items])
