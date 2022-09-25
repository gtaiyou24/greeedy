from injector import inject

from domain.model.color import Color
from domain.model.item.image import ItemImageService, ItemImage
from domain.model.url import URL
from port.adapter.service.item.image.adapter import ItemImageAdapter


class ItemImageServiceImpl(ItemImageService):
    @inject
    def __init__(self, item_image_adapter: ItemImageAdapter):
        self.__item_image_adapter = item_image_adapter

    def estimate(self, image_urls: list[URL], colors: set[Color]) -> list[ItemImage]:
        return self.__item_image_adapter.estimate(image_urls, colors)
