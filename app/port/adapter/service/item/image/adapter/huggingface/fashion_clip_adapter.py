import json

import requests
from injector import singleton
from slf4py import set_logger

from domain.model.color import Color
from domain.model.item import ItemName
from domain.model.url import URL
from port.adapter.service.item.image.adapter import ColorAdapter


@set_logger
@singleton
class FashionCLIPAdapter(ColorAdapter):
    def estimate(self, image_urls: list[URL], item_name: ItemName, option_colors: set[Color]) -> list[Color]:
        colors = option_colors if option_colors else Color
        res = requests.post(
            'https://fashion-clip.2b2vm44ekho8i.ap-northeast-1.cs.amazonlightsail.com/invocations',
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            data=json.dumps({
                'mode': 'image_classification',
                'texts': [f'{color.value} {item_name.text}' for color in colors],
                'images': [image_url.address for image_url in image_urls]
            })
        )
        self.log.debug(f'{res.status_code} : {res.json()}')
        if res.status_code != 200:
            raise Exception('Fashion CLIP との通信に失敗しました。')

        colors = []
        for i, labels in enumerate(res.json()):
            k = max(labels, key=labels.get)
            label = k.split(' ')[0]
            colors.append(Color.value_of(label))
        return colors
