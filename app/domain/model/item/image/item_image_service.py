import abc

from domain.model.item.image import ItemImage
from domain.model.url import URL


class ItemImageService(abc.ABC):
    @abc.abstractmethod
    def estimate(self, image_urls: list[URL]) -> list[ItemImage]:
        pass
