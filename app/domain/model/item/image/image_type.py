from __future__ import annotations

from enum import Enum


class ImageType(Enum):
    ITEM_ANGLED = "pack-angled"
    ITEM_BACK = "pack-back"
    ITEM_BOTTOM = "pack-bottom"
    ITEM_DETAIL = "pack-detail"
    ITEM_FRONT = "pack-front"
    ITEM_SIDE = "pack-side"
    ITEM_TOP = "pack-top"
    MODEL_BACK_CLOSE = 'model-back-close'
    MODEL_BACK_FULL = "model-back-full"
    MODEL_DETAIL = "model-detail"
    MODEL_FRONT_CLOSE = "model-front-close"
    MODEL_FRONT_FULL = "model-front-full"
    MODEL_SIDE_CLOSE = "model-side-close"
    MODEL_SIDE_FULL = "model-side-full"
    UNKNOWN = 'unknown'

    @classmethod
    def value_of(cls, value: str) -> ImageType:
        for e in cls:
            if e.value == value:
                return e
        raise ValueError(f'値が{value}のImageTypeが見つかりませんでした。')
