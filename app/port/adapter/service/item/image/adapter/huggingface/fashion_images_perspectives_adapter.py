import requests
from injector import singleton
from slf4py import set_logger

from domain.model.color import Color
from domain.model.item.image import ImageType
from domain.model.url import URL
from port.adapter.service.item.image.adapter import ImageTypeAdapter


@set_logger
@singleton
class FashionImagesPerspectivesAdapter(ImageTypeAdapter):
    API_URL = "https://api-inference.huggingface.co/models/touchtech/fashion-images-perspectives-vit-large-patch16-224-in21k"

    def __init__(self, api_token: str):
        self.__api_token = api_token

    def estimate(self, image_urls: list[URL], colors: set[Color]) -> list[ImageType]:
        image_types = []
        for image_url in image_urls:
            img = requests.get(image_url.address, stream=True).content
            res = requests.post(self.API_URL, headers={"Authorization": f"Bearer {self.__api_token}"}, data=img)
            self.log.debug(f'{res.status_code} : {res.json()}')
            if res.status_code != 200:
                image_types.append(ImageType.UNKNOWN)
            label = res.json()[0]['label']
            image_types.append(ImageType.value_of(label))
        return image_types
