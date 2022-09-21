from __future__ import annotations

from pydantic import BaseModel, Field

from application.category.dpo import GetCategoryDpo


class GetCategoryJson(BaseModel):
    class Query(BaseModel):
        text: str = Field(title='テキスト')
        operator: str = Field(title='オペレーション')

    id: str = Field(title='カテゴリID')
    gender: str = Field(title='性別')
    name: str = Field(title='カテゴリ名')
    image_url: str = Field(title='画像URL')
    sub_category_ids: list[str] = Field(title='サブカテゴリIDの一覧')
    operator_and_queries: dict[str, list[GetCategoryJson.Query]] = Field(
        default={}, title='クエリセット', description='ex) {"or": [{"text": "検索テキスト", "operator": "and"}]}')

    @staticmethod
    def of(dpo: GetCategoryDpo) -> GetCategoryJson:
        return GetCategoryJson(
            id=dpo.category.id.value,
            gender=dpo.category.gender.name,
            name=dpo.category.name.text,
            image_url=dpo.category.image_url.address,
            sub_category_ids=[_id.value for _id in dpo.category.sub_category_ids],
            operator_and_queries={operator.value: [{'text': q.text, 'operator': q.operator.value} for q in queries] \
                                  for operator, queries in dpo.category.query_set.all.items()}
        )
