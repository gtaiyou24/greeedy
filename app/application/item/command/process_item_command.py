from dataclasses import dataclass


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
    colors: set[str]
    price: float
    description: str
    gender: str
    images: list[Image]
    url: str
    meta: Meta
