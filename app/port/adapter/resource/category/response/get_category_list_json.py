from __future__ import annotations

from pydantic import BaseModel, Field

from application.category.dpo import GetCategoryListDpo, GetCategoryDpo
from port.adapter.resource.category.response import GetCategoryJson


class GetCategoryListJson(BaseModel):
    results: list[GetCategoryJson] = Field(title='カテゴリ一覧')

    @staticmethod
    def of(dpo: GetCategoryListDpo) -> GetCategoryListJson:
        return GetCategoryListJson(results=[
            GetCategoryJson.of(GetCategoryDpo(category=category)) for category in dpo.category_list])
