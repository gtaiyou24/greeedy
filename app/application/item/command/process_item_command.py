from dataclasses import dataclass
from typing import List, Optional


@dataclass(unsafe_hash=True, frozen=True)
class ProcessItemCommand:
    @dataclass(unsafe_hash=True, frozen=True)
    class Meta:
        keywords: str
        description: str

    @dataclass(unsafe_hash=True, frozen=True)
    class Image:
        url: str

    name: str
    brand_name: str
    price: float
    description: str
    gender: str
    images: List[Image]
    url: str
    meta: Meta
