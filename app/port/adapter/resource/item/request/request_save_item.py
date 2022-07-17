from __future__ import annotations

from typing import Optional, List

from pydantic import BaseModel, Field


class RequestSaveItem(BaseModel):
    class Meta(BaseModel):
        keywords: str = Field(default="", description="メタ情報のキーワード")
        description: str = Field(default="", description="メタ情報の説明文")
        content: str = Field(default="", description="HTMLのコンテンツ")

    id: Optional[str] = Field(default=None, title="アイテムID", description="未指定の場合はIDを自動生成します")
    name: str = Field(title="アイテム名")
    brand_name: str = Field(title="ブランド名")
    price: int = Field(title="価格", ge=0)
    gender: str = Field(default="WOMEN", title="性別", description="WOMEN=レディース, MEN=メンズ, KIDS=キッズ, UNISEX=ユニセックス")
    images: List[str] = Field(title="アイテムの画像一覧", regex=r"^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")
    url: str = Field(title="アイテムのページURL", regex=r"^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")
    meta: RequestSaveItem.Meta
