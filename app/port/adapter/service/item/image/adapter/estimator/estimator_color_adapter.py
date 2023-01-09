import os

import boto3
import sagemaker
from injector import singleton, inject
from sagemaker import Predictor
from slf4py import set_logger

from domain.model.color import Color
from domain.model.item import ItemName
from domain.model.url import URL
from port.adapter.service.item.image.adapter import ColorAdapter
from port.adapter.service.item.image.adapter.estimator.translator import ColorTranslator


@set_logger
@singleton
class EstimatorColorAdapter(ColorAdapter):
    @inject
    def __init__(self, color_translator: ColorTranslator):
        self.__color_translator = color_translator
        self.__sagemaker_predictor = Predictor(
            endpoint_name='greeedy-estimator',
            sagemaker_session=sagemaker.Session(boto_session=boto3.Session(profile_name=os.environ.get("AWS_PROFILE"))),
            serializer=sagemaker.serializers.JSONSerializer(),
            deserializer=sagemaker.deserializers.JSONDeserializer(),
        )

    def estimate(self, image_urls: list[URL], item_name: ItemName, option_colors: set[Color]) -> list[Color]:
        try:
            payload = {
                'item_name': item_name.text,
                'image_urls': [image_url.address for image_url in image_urls],
                'option_colors': [color.value for color in option_colors]
            }
            self.log.debug(f"payload = {payload}")
            response = self.__sagemaker_predictor.predict(payload)
            self.log.debug(f"response = {response}")
            return self.__color_translator.from_(response)
        except Exception as e:
            self.log.error(e)
            raise e
