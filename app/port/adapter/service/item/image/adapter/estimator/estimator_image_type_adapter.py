import json

import requests
from injector import inject, singleton
from slf4py import set_logger

from domain.model.color import Color
from domain.model.item.image import ImageType
from domain.model.url import URL
from exception import SystemException, ErrorCode
from port.adapter.service.item.image.adapter import ImageTypeAdapter
from port.adapter.service.item.image.adapter.estimator.translator import ImageTypeTranslator


@set_logger
@singleton
class EstimatorImageTypeAdapter(ImageTypeAdapter):
    @inject
    def __init__(self, image_type_translator: ImageTypeTranslator):
        self.__image_type_translator = image_type_translator
        self.__estimate_image_url = "https://xytidfd57l.execute-api.ap-northeast-1.amazonaws.com/dev/images"
        self.__connection_timeout = 30.0
        self.__read_timeout = 120.0

    def estimate(self, image_urls: list[URL], colors: set[Color]) -> list[ImageType]:
        payload = {
            'image_urls': [image_url.address for image_url in image_urls],
            'option_colors': [color.value for color in colors]
        }
        self.log.debug(f'payload = {payload}')
        try:
            response = requests.post(self.__estimate_image_url,
                                     data=json.dumps(payload),
                                     headers={'Content-Type': 'application/json'})
            self.log.debug(f"response = {response}")
            return self.__image_type_translator.from_(response.json())
        except ConnectionError as e:
            raise SystemException(ErrorCode.GREEEDY_ML_CONNECTION_ERROR,
                                  f'url = {self.__estimate_image_url}, error = {str(e)}')
        except TimeoutError as e:
            raise SystemException(ErrorCode.GREEEDY_ML_TIME_OUT,
                                  f'url = {self.__estimate_image_url}, error = {str(e)}')
        except requests.exceptions.RequestException as e:
            raise SystemException(ErrorCode.GREEEDY_ML_REQUEST_ERROR,
                                  f'url = {self.__estimate_image_url}, error = {str(e)}')
        except Exception as e:
            self.log.error(e)
