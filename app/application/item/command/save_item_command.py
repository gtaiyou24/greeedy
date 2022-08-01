from dataclasses import dataclass
from typing import List, Optional


@dataclass(unsafe_hash=True, frozen=True)
class SaveItemCommand:
    @dataclass(unsafe_hash=True, frozen=True)
    class Meta:
        keywords: str
        description: str

    @dataclass(unsafe_hash=True, frozen=True)
    class Image:
        type: str
        color: str
        url: str

    id: Optional[str]
    name: str
    brand_name: str
    price: float
    description: str
    gender: str
    images: List[Image]
    url: str
    meta: Meta

    def is_id_empty(self) -> bool:
        return self.id is None
