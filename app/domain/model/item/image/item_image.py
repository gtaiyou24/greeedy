from dataclasses import dataclass
from enum import Enum

from domain.model.url import URL


class ImageType(Enum):
    MODEL_WEARING = "モデル着用画像"
    ONLY_ITEM = "アイテムのみ画像"
    ZOOM_IN = "ズームアップ画像"
    OTHER = "その他"


class Color:
    pass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class ItemImage:
    type: ImageType
    # color: Color
    url: URL

    def __init__(self, type: ImageType, url: URL):
        assert isinstance(type, ImageType), "画像タイプは必須です"
        assert isinstance(url, URL), "画像URLは必須です"
        super().__setattr__("type", type)
        super().__setattr__("url", url)
