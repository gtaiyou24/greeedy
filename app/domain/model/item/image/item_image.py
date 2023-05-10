from dataclasses import dataclass

from domain.model.color import Color
from domain.model.item.image import ImageType, ImagePath
from domain.model.url import URL


@dataclass(init=False, unsafe_hash=True, frozen=True)
class ItemImage:
    type: ImageType
    color: Color
    url: URL
    thumbnail: ImagePath

    def __init__(self, type: ImageType, color: Color, url: URL, thumbnail: ImagePath):
        assert isinstance(type, ImageType), "画像タイプは必須です"
        assert isinstance(color, Color), "カラーは必須です"
        assert isinstance(url, URL), "画像URLは必須です"
        assert isinstance(thumbnail, ImagePath), "サムネイル画像は必須です"
        super().__setattr__("type", type)
        super().__setattr__("color", color)
        super().__setattr__("url", url)
        super().__setattr__("thumbnail", thumbnail)
