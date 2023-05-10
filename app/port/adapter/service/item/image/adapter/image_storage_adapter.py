import abc
from io import BytesIO
from typing import Optional

from domain.model.item.image import ImagePath


class ImageStorageAdapter(abc.ABC):
    @abc.abstractmethod
    def upload(self, filename: str, buffer: BytesIO, content_type: str) -> Optional[ImagePath]:
        pass
