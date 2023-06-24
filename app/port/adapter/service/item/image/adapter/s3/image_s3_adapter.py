from io import BytesIO
from typing import Optional

import boto3
from injector import singleton, inject
from slf4py import set_logger

from domain.model.item.image import ImagePath
from port.adapter.service.item.image.adapter import ImageStorageAdapter


@set_logger
@singleton
class ImageS3Adapter(ImageStorageAdapter):
    @inject
    def __init__(self):
        self.__s3 = boto3.client('s3', region_name='ap-northeast-1')

    def upload(self, filename: str, buffer: BytesIO, content_type: str) -> Optional[ImagePath]:
        image_path = ImagePath(f'/items/{filename}')
        try:
            self.log.debug(f'画像({image_path.file_path})をS3にアップロードします...')
            self.__s3.put_object(Bucket='greeedy', Key=image_path.file_path[1:], Body=buffer, ContentType=content_type)
        except Exception as e:
            self.log.error(e)
            return None

        self.log.debug(f'画像({image_path.file_path})をアップロードしました')
        return image_path
