from fastapi import APIRouter

from application.category.service import CategoryApplicationService
from di import DIManager
from port.adapter.resource.category.response import GetCategoryTreeListJson

router = APIRouter(
    prefix="/categories",
    tags=["カテゴリ系"]
)

category_application_service = DIManager.get(CategoryApplicationService)


@router.get("/{gender}", response_model=GetCategoryTreeListJson, name="カテゴリツリー取得機能")
def get(gender: str) -> GetCategoryTreeListJson:
    dpo = category_application_service.get_category_tree_list(gender)
    return GetCategoryTreeListJson.make_by(dpo)
