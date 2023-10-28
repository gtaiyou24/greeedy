import os

import boto3
import sagemaker
from injector import singleton
from sagemaker import Predictor
from slf4py import set_logger

from domain.model.color import Color
from domain.model.item import ItemName
from domain.model.url import URL
from port.adapter.service.item.image.adapter import ColorAdapter


@set_logger
@singleton
class FashionClipAdapter(ColorAdapter):
    def __init__(self):
        self.__sagemaker_predictor = Predictor(
            endpoint_name='fashion-clip',
            sagemaker_session=sagemaker.Session(boto_session=boto3.Session(profile_name=os.environ.get("AWS_PROFILE"))),
            serializer=sagemaker.serializers.JSONSerializer(),
            deserializer=sagemaker.deserializers.JSONDeserializer(),
        )

    def estimate(self, image_urls: list[URL], item_name: ItemName, option_colors: set[Color]) -> list[Color]:
        try:
            colors = option_colors if option_colors else Color
            payload = {
                'mode': 'image_classification',
                'texts': [f'{color.value} {item_name.text}' for color in colors],
                'images': [image_url.address for image_url in image_urls]
            }
            self.log.debug(f"payload = {payload}")
            response = self.__sagemaker_predictor.predict(payload)
            self.log.debug(f"response = {response}")
            colors = []
            for i, labels in enumerate(response):
                k = max(labels, key=labels.get)
                label = k.split(' ')[0]
                colors.append(Color.value_of(label))
            return colors
        except Exception as e:
            self.log.error(e)
            raise e
