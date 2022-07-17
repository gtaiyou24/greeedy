from dataclasses import dataclass
from typing import List

from domain.model.item.image import ItemImage


@dataclass(init=False, unsafe_hash=True, frozen=True)
class ItemImageList:
    list: List[ItemImage]

    def __init__(self, images: List[ItemImage]):
        assert isinstance(images, list), "画像一覧にはListを指定してください"
        assert len(images) == len(set(images)), "画像が重複しています"
        super().__setattr__("list", images)
