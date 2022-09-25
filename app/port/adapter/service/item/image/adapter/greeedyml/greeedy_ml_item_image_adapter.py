import json

import requests
from injector import inject, singleton
from slf4py import set_logger

from domain.model.color import Color
from domain.model.item.image import ItemImage
from domain.model.url import URL
from exception import SystemException, ErrorCode
from port.adapter.service.item.image.adapter import ItemImageAdapter
from port.adapter.service.item.image.adapter.greeedyml.translator import EstimateTranslator


@set_logger
@singleton
class GreeedyMLItemImageAdapter(ItemImageAdapter):
    @inject
    def __init__(self, estimate_translator: EstimateTranslator):
        self.__estimate_translator = estimate_translator
        self.__estimate_image_url = "https://xytidfd57l.execute-api.ap-northeast-1.amazonaws.com/dev/images"
        self.__connection_timeout = 30.0
        self.__read_timeout = 120.0

    def estimate(self, image_urls: list[URL], colors: set[Color]) -> list[ItemImage]:
        payload = {
            'image_urls': [image_url.address for image_url in image_urls],
            'option_colors': [color.value for color in colors]
        }
        self.log.debug(f'payload = {payload}')
        try:
            response = requests.post(self.__estimate_image_url,
                                     data=json.dumps(payload),
                                     headers={'Content-Type': 'application/json'})
            item_image_list = self.__estimate_translator.from_(response.json())
            self.log.debug(f"response = {item_image_list}")
            return item_image_list
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
