from fastapi import APIRouter

from di import DIContainer

from application.category.command import SaveCategoryCommand
from application.category.service import CategoryApplicationService
from port.adapter.resource.category.request import RequestSaveCategory
from port.adapter.resource.category.response import GetCategoryTreeListJson, GetCategoryJson

router = APIRouter(
    prefix="/categories",
    tags=["カテゴリ系"]
)


@router.get("/tree/{gender}", response_model=GetCategoryTreeListJson, name="カテゴリツリー取得機能")
def tree(gender: str) -> GetCategoryTreeListJson:
    category_application_service = DIContainer.instance().resolve(CategoryApplicationService)
    dpo = category_application_service.get_category_tree(gender)
    return GetCategoryTreeListJson.make_by(dpo)


@router.post("/", name="カテゴリ保存機能")
def save(request: RequestSaveCategory):
    category_application_service = DIContainer.instance().resolve(CategoryApplicationService)
    command = SaveCategoryCommand(
        id=request.id,
        gender=request.gender,
        name=request.name,
        image_url=request.image_url,
        sub_category_ids=request.sub_category_ids,
        operator_and_queries={
            operator: {SaveCategoryCommand.Query(text=q.text, operator=q.operator) for q in queries} \
            for operator, queries in request.operator_and_queries.items()}
    )
    category_application_service.save(command)


@router.get("/{category_id}", response_model=GetCategoryJson, name="カテゴリ取得機能")
def get(category_id: str) -> GetCategoryJson:
    category_application_service = DIContainer.instance().resolve(CategoryApplicationService)
    dpo = category_application_service.get_category(category_id)
    return GetCategoryJson.of(dpo)
