import abc

from domain.model.color import Color
from domain.model.item import ItemName
from domain.model.item.image import ImageType
from domain.model.url import URL


class ItemImageService(abc.ABC):
    @abc.abstractmethod
    def estimate(self, image_urls: list[URL], item_name: ItemName, option_colors: set[Color]) -> list[tuple[ImageType, Color]]:
        pass
