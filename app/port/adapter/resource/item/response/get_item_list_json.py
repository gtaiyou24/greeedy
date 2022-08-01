from __future__ import annotations

from typing import List

from pydantic import BaseModel, Field

from application.item.dpo import GetItemListDpo, GetItemDpo
from port.adapter.resource.item.response import GetItemJson


class GetItemListJson(BaseModel):
    items: List[GetItemJson] = Field(title="アイテム一覧")

    @staticmethod
    def make_by(dpo: GetItemListDpo) -> GetItemListJson:
        return GetItemListJson(items=[GetItemJson.make_by(GetItemDpo(item)) for item in dpo.items])
