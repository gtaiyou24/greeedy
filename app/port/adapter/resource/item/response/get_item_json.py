from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from application.item.dpo import GetItemDpo


class GetItemJson(BaseModel):
    class ItemPrice(BaseModel):
        amount: float = Field(default=100, title="価格")
        currency: str = Field(default="yen", title="通貨単位")
        type: str = Field(default="NORMAL_PRICE", title="価格種別", description="NORMAL_PRICE=通常価格")

    class ItemImage(BaseModel):
        type: str = Field(default="MODEL_WEARING", title="画像種別", description="MODEL_WEARING=モデル着用画像")
        color: str = Field(default="WHITE", title="カラー")
        url: str = Field(title="画像URL")

    id: str = Field(description="アイテムID")
    name: str = Field(description="アイテム名")
    brand_name: str = Field(description="ブランド名")
    # price: List[GetItemJson.ItemPrice] = Field(description="価格")
    price: int = Field(description="価格")
    description: str = Field(description="アイテムの説明文")
    gender: str = Field(description="性別")
    images: List[GetItemJson.ItemImage] = Field(description="画像URL一覧")
    url: str = Field(description="アイテムのページURL")

    @staticmethod
    def make_by(dpo: GetItemDpo) -> GetItemJson:
        return GetItemJson(id=dpo.item.id.value, name=dpo.item.name.text, brand_name=dpo.item.brand_name.text,
                           price=dpo.item.price.amount,
                           description=dpo.item.description.text,
                           gender=dpo.item.gender.name,
                           images=[
                               GetItemJson.ItemImage(type=image.type.name, color=image.color.name, url=image.url.address) \
                               for image in dpo.item.images.list
                           ],
                           url=dpo.item.page.url.address)
