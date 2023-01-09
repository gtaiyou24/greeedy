from typing import NoReturn

from injector import singleton, inject

from application.item.command import ProcessItemCommand
from domain.model.color import Color
from domain.model.gender import Gender
from domain.model.item import Item, ItemName, BrandName, Price, Description, ItemIndex
from domain.model.item.id import ItemIdFactory
from domain.model.item.image import ItemImageList, ItemImageService
from domain.model.page import Page
from domain.model.url import URL


@singleton
class ProcessItemApplicationService:
    @inject
    def __init__(self, item_id_factory: ItemIdFactory, item_image_service: ItemImageService, item_index: ItemIndex):
        self.__item_id_factory = item_id_factory
        self.__item_image_service = item_image_service
        self.__item_index = item_index

    def process(self, command: ProcessItemCommand) -> NoReturn:
        item_id = self.__item_id_factory.make(command.url)
        item_name = ItemName(command.name)

        images = self.__item_image_service.estimate([URL(image.url) for image in command.images],
                                                    item_name,
                                                    {Color.value_of(color) for color in command.colors})

        item = Item(
            item_id, item_name, BrandName(command.brand_name), Price(command.price, Price.Currency.JPY),
            Description(command.description), Gender[command.gender], ItemImageList(images).sort(),
            Page(URL(command.url), command.meta.keywords, command.meta.description))

        self.__item_index.add(item)
