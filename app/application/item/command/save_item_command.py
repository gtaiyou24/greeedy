from dataclasses import dataclass
from typing import List, Optional


@dataclass(unsafe_hash=True, frozen=True)
class SaveItemCommand:
    @dataclass(unsafe_hash=True, frozen=True)
    class Meta:
        keywords: str
        description: str
        content: str

    id: Optional[str]
    name: str
    brand_name: str
    price: float
    gender: str
    images: List[str]
    url: str
    meta: Meta

    def is_id_empty(self) -> bool:
        return self.id is None
