from injector import inject

from domain.model.color import Color
from domain.model.item import ItemName
from domain.model.item.image import ItemImageService, ItemImage
from domain.model.url import URL
from port.adapter.service.item.image.adapter import ImageTypeAdapter, ColorAdapter


class ItemImageServiceImpl(ItemImageService):
    @inject
    def __init__(self, color_adapter: ColorAdapter, image_type_adapter: ImageTypeAdapter):
        self.__color_adapter = color_adapter
        self.__image_type_adapter = image_type_adapter

    def estimate(self, image_urls: list[URL], item_name: ItemName, option_colors: set[Color]) -> list[ItemImage]:
        return [ItemImage(image_type, color, url) for image_type, color, url in zip(
            self.__image_type_adapter.estimate(image_urls, option_colors),
            self.__color_adapter.estimate(image_urls, item_name, option_colors),
            image_urls
        )]
