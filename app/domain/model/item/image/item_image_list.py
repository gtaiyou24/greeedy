from __future__ import annotations

from dataclasses import dataclass
from typing import List

from domain.model.item.image import ItemImage, ImageType


@dataclass(init=False, unsafe_hash=True, frozen=True)
class ItemImageList:
    list: List[ItemImage]

    def __init__(self, images: List[ItemImage]):
        assert images, "画像一覧は必須です。"
        assert isinstance(images, List), "画像一覧に{type}が指定されています。List型を指定してください。".format(type=type(images))
        assert len(images) == len(set(images)), "画像が重複しています。"
        super().__setattr__("list", images)

    def sort(self) -> ItemImageList:
        image_types = {ImageType.ZOOM_IN}
        if self.__has_only(image_types):
            return self

        sorted_images = self.list
        for i in range(len(self.list)):
            if sorted_images[i].type not in image_types:
                return ItemImageList(sorted_images)
            image = sorted_images.pop(i)
            sorted_images.append(image)

        return ItemImageList(sorted_images)

    def __has_only(self, image_types: set[ImageType]) -> bool:
        return {image.type for image in self.list} == image_types
