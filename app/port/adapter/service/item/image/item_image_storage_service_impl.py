import hashlib
import io
from typing import Optional

from injector import inject
from requests import Session
from slf4py import set_logger
from PIL import Image

from domain.model.item.image import ItemImageStorageService, ImagePath
from domain.model.url import URL
from port.adapter.service.item.image.adapter import ImageStorageAdapter


@set_logger
class ItemImageStorageServiceImpl(ItemImageStorageService):
    @inject
    def __init__(self, image_storage_adapter: ImageStorageAdapter, session: Session):
        self.__image_storage_adapter = image_storage_adapter
        self.__session = session

    def upload(self, image_url: URL, size: tuple[int, int]) -> Optional[ImagePath]:
        response = self.__session.get(url=image_url.address, stream=True, timeout=(10.0, 30.0))

        image: Image.Image = Image.open(io.BytesIO(response.content))
        content_type = response.headers["Content-Type"]

        # exif情報からOrientation値を取得し、回転方法を決定する
        image = self.__transpose(image)

        # サムネイル画像を作成
        extension = content_type[6:]
        buffer = self.__make_thumbnail(image, extension, size[0], image.height)

        return self.__image_storage_adapter.upload(
            f"{hashlib.sha256(image_url.address.encode()).hexdigest()}.{extension}",
            buffer,
            content_type
        )

    def __transpose(self, image: Image.Image) -> Image.Image:
        exif = image.getexif()
        orientation = exif.get(0x112, 1)
        convert_image = {
            1: lambda img: img,  # そのまま
            2: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),  # 左右反転
            3: lambda img: img.transpose(Image.ROTATE_180),  # 180度回転
            4: lambda img: img.transpose(Image.FLIP_TOP_BOTTOM),  # 上下反転
            5: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90),  # 左右反転＆反時計回りに90度回転
            6: lambda img: img.transpose(Image.ROTATE_270),  # 反時計回りに270度回転
            7: lambda img: img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270),  # 左右反転＆反時計回りに270度回転
            8: lambda img: img.transpose(Image.ROTATE_90),  # 反時計回りに90度回転
        }
        return convert_image[orientation](image)

    def __make_thumbnail(self, image: Image.Image, extension: str, width: int, height: int) -> io.BytesIO:
        image.thumbnail(size=(width, height), resample=Image.BOX)
        buffer = io.BytesIO()
        image.save(buffer, extension)
        buffer.seek(0)
        return buffer
