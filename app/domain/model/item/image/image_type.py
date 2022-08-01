from enum import Enum


class ImageType(Enum):
    MODEL_WEARING = "モデル着用画像"
    ONLY_ITEM = "アイテムのみ画像"
    ZOOM_IN = "ズームアップ画像"
    OTHER = "その他"
