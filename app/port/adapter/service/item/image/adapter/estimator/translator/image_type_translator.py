from domain.model.item.image import ImageType


class ImageTypeTranslator:
    def __init__(self):
        self.__types = {
            0: ImageType.MODEL_WEARING,
            1: ImageType.ONLY_ITEM,
            2: ImageType.ZOOM_IN,
            -1: ImageType.OTHER
        }

    def from_(self, response: dict) -> list[ImageType]:
        return [self.__types[image['type']] for image in response['images']]
