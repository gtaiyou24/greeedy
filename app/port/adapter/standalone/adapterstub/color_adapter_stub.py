from domain.model.color import Color
from domain.model.item import ItemName
from domain.model.url import URL
from port.adapter.service.item.image.adapter import ColorAdapter


class ColorAdapterStub(ColorAdapter):
    def estimate(self, image_urls: list[URL], item_name: ItemName, option_colors: set[Color]) -> list[Color]:
        return [Color.WHITE for url in image_urls]
