from domain.model.color import Color
from domain.model.item.image import ItemImage, ImageType
from domain.model.url import URL


class EstimateTranslator:
    def __init__(self):
        self.__types = {
            0: ImageType.MODEL_WEARING,
            1: ImageType.ONLY_ITEM,
            2: ImageType.ZOOM_IN,
            -1: ImageType.OTHER
        }

    def from_(self, response: dict) -> list[ItemImage]:
        item_image_list = []
        for image in response['images']:
            item_image_list.append(
                ItemImage(type=self.__types[image['type']], color=Color.value_of(image['color']), url=URL(image['url']))
            )
        return item_image_list
