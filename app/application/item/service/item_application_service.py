from injector import inject, singleton

from application.item.command import SaveItemCommand
from application.item.dpo import GetItemDpo
from domain.model.gender import Gender
from domain.model.item import ItemRepository, Item, ItemName, BrandName, Price, ItemIndex
from domain.model.item.id import ItemId, ItemIdFactory
from domain.model.item.image import ItemImageList, ItemImage
from domain.model.item.meta import Meta
from domain.model.url import URL
from exception import SystemException, ErrorCode


@singleton
class ItemApplicationService:
    @inject
    def __init__(self, item_repository: ItemRepository,
                 item_index: ItemIndex,
                 item_id_factory: ItemIdFactory):
        self.__item_repository = item_repository
        self.__item_index = item_index
        self.__item_id_factory = item_id_factory

    def save(self, command: SaveItemCommand):
        if command.is_id_empty():
            item_id = self.__item_id_factory.make(command.url)
        else:
            item_id = ItemId(command.id)

        meta = Meta(Meta.MetaName.keywords, command.meta.keywords)
        meta.set_other_meta(Meta(Meta.MetaName.description, command.meta.description))
        meta.set_other_meta(Meta(Meta.MetaName.content, command.meta.content))

        item = Item(item_id, ItemName(command.name), BrandName(command.brand_name),
                    Price(command.price, Price.Currency.yen), Gender[command.gender],
                    ItemImageList([ItemImage(URL(image_url)) for image_url in command.images]),
                    URL(command.url), meta)

        self.__item_repository.save(item)
        self.__item_index.add(item)

    def get(self, an_id: str) -> GetItemDpo:
        item_id = ItemId(an_id)
        optional_item = self.__item_repository.item_of(item_id)

        if optional_item is None:
            raise SystemException(ErrorCode.ITEM_NOT_FOUND, "アイテムID={}".format(item_id.value))

        return GetItemDpo(optional_item)

    def delete(self, an_id: str):
        item_id = ItemId(an_id)
        self.__item_repository.delete(item_id)
        self.__item_index.delete(item_id)
