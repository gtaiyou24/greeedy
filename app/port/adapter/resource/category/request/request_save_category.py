from pydantic import BaseModel, Field


class RequestSaveCategory(BaseModel):
    class Query(BaseModel):
        text: str
        operator: str

    id: str = Field(default='', title='カテゴリID', regex=r'[0-9A-Za-z-]+')
    gender: str = Field(default='', title='性別')
    name: str = Field(default='', title='カテゴリ名')
    image_url: str = Field(default='', title='カテゴリ画像URL', regex=r'^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+')
    sub_category_ids: list[str] = Field(default=[], title='サブカテゴリID一覧')
    operator_and_queries: dict[str, list[Query]] = Field(
        default={}, title='クエリセット', description='ex) {"or": [{"text": "検索テキスト", "operator": "and"}]}')
