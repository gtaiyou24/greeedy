from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel, Field


class RequestSaveItem(BaseModel):
    class Meta(BaseModel):
        keywords: str = Field(default="", description="メタ情報のキーワード")
        description: str = Field(default="", description="メタ情報の説明文")

    class Image(BaseModel):
        type: str = Field(title="画像タイプ")
        color: str = Field(title="アイテムカラー")
        thumbnail: Optional[str] = Field(title="サムネイル画像のファイルパス")
        url: str = Field(title="アイテムの画像のURL", regex=r"^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")

    id: Optional[str] = Field(default=None, title="アイテムID", description="未指定の場合はIDを自動生成します")
    name: str = Field(title="アイテム名")
    brand_name: str = Field(title="ブランド名")
    price: int = Field(title="価格", ge=0)
    description: str = Field(default="", description="アイテムの説明文")
    gender: str = Field(default="WOMEN", title="性別", description="WOMEN=レディース, MEN=メンズ, KIDS=キッズ, UNISEX=ユニセックス")
    images: List[RequestSaveItem.Image] = Field(title="アイテムの画像一覧")
    url: str = Field(title="アイテムのページURL", regex=r"^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")
    meta: RequestSaveItem.Meta
