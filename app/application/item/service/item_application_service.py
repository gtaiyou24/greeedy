from typing import List

from injector import inject, singleton

from application.item.command import SaveItemCommand
from application.item.dpo import GetItemDpo, GetItemListDpo
from domain.model.color import Color
from domain.model.gender import Gender
from domain.model.item import Item, ItemName, BrandName, Price, ItemIndex, Description
from domain.model.item.id import ItemId, ItemIdFactory
from domain.model.item.image import ItemImageList, ItemImage, ImageType
from domain.model.page import Page
from domain.model.url import URL
from exception import SystemException, ErrorCode


@singleton
class ItemApplicationService:
    @inject
    def __init__(self,
                 item_index: ItemIndex,
                 item_id_factory: ItemIdFactory):
        self.__item_index = item_index
        self.__item_id_factory = item_id_factory

    def save(self, command: SaveItemCommand):
        if command.is_id_empty():
            item_id = self.__item_id_factory.make(command.url)
        else:
            item_id = ItemId(command.id)

        item = Item(
            item_id, ItemName(command.name), BrandName(command.brand_name),
            Price(command.price, Price.Currency.JPY),
            Description(command.description), Gender[command.gender],
            ItemImageList(
                [ItemImage(ImageType[image.type], Color[image.color], URL(image.url)) for image in command.images]
            ),
            Page(URL(command.url), command.meta.keywords, command.meta.description))

        self.__item_index.add(item)

    def get(self, an_item_id: str) -> GetItemDpo:
        optional_item = self.__item_index.get(ItemId(an_item_id))

        if optional_item is None:
            raise SystemException(ErrorCode.ITEM_NOT_FOUND, "アイテムID={}".format(an_item_id))

        return GetItemDpo(optional_item)

    def list(self, an_item_ids: List[str]) -> GetItemListDpo:
        items = []
        for _id in an_item_ids:
            item = self.__item_index.get(ItemId(_id))
            if item:
                items.append(item)
        return GetItemListDpo(items)

    def delete(self, an_item_id: str):
        item_id = ItemId(an_item_id)
        self.__item_index.delete(item_id)
