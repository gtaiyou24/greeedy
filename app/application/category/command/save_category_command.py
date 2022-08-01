from dataclasses import dataclass
from typing import List, Set


@dataclass(unsafe_hash=True, frozen=True)
class SaveCategoryCommand:
    @dataclass(unsafe_hash=True, frozen=True)
    class Query:
        text: str
        operator: str

    id: str
    gender: str
    name: str
    image_url: str
    sub_category_ids: List[str]
    operator_and_queries: dict[str:Set[Query]]
