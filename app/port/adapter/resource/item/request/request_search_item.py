from __future__ import annotations

from typing import Set, Optional

from pydantic import BaseModel, Field


class RequestSearchItem(BaseModel):
    class PriceRange(BaseModel):
        price_from: Optional[int] = Field(default=None, title="価格下限", ge=0)
        price_to: Optional[int] = Field(default=None, title="価格上限")

    gender: str = Field(default="WOMEN", title="性別", description="WOMEN=レディース, MEN=メンズ, KIDS=キッズ, UNISEX=ユニセックス")
    keyword: Optional[str] = Field(default=None, title="キーワード")
    category: Optional[str] = Field(default=None, title="カテゴリ")
    colors: Set[str] = Field(default=set(), title="カラー一覧")
    designs: Set[str] = Field(default=set(), title="柄・デザイン一覧")
    details: Set[str] = Field(default=set(), title="こだわり条件一覧")
    price_range: RequestSearchItem.PriceRange = Field(default=PriceRange(), title="価格範囲")
    sort: str = Field(default="relevance", title="並び順")
    start: int = Field(default=1, title="開始位置", description="検索結果のうち何件目から取得するか")
    size: int = Field(default=20, title="件数")
