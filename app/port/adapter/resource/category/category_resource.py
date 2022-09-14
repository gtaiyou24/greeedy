from fastapi import APIRouter

from di import DIContainer

from application.category.service import CategoryApplicationService
from port.adapter.resource.category.response import GetCategoryTreeListJson

router = APIRouter(
    prefix="/categories",
    tags=["カテゴリ系"]
)


@router.get("/{gender}", response_model=GetCategoryTreeListJson, name="カテゴリツリー取得機能")
def get(gender: str) -> GetCategoryTreeListJson:
    category_application_service = DIContainer.instance().resolve(CategoryApplicationService)
    dpo = category_application_service.get_category_tree_list(gender)
    return GetCategoryTreeListJson.make_by(dpo)
