import abc
from typing import Optional

from domain.model.item.image import ImagePath
from domain.model.url import URL


class ItemImageStorageService(abc.ABC):
    @abc.abstractmethod
    def upload(self, image_url: URL, size: tuple[int, int]) -> Optional[ImagePath]:
        pass
