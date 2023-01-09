import abc

from domain.model.color import Color
from domain.model.item.image import ImageType
from domain.model.url import URL


class ImageTypeAdapter(abc.ABC):
    @abc.abstractmethod
    def estimate(self, image_urls: list[URL], colors: set[Color]) -> list[ImageType]:
        pass
