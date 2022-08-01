from typing import Optional, List

from injector import inject

from domain.model.gender import Gender
from domain.model.item import Item, ItemName, BrandName, Price
from domain.model.item.id import ItemId
from domain.model.item.image import ItemImageList, ItemImage
from domain.model.url import URL
from port.adapter.persistence.repository.mysql.item.driver import ItemsCrud, ItemsTableRow


class DriverManagerItem:
    @inject
    def __init__(self, items_crud: ItemsCrud):
        self.__items_crud = items_crud

    def find_by_id(self, id: ItemId) -> Optional[Item]:
        optional: Optional[ItemsTableRow] = self.__items_crud.find_by_id(id.value)
        if optional is None:
            return None
        return self.__generate_item_from(optional)

    def find_all_by_ids(self, ids: List[ItemId]) -> List[Item]:
        table_rows: List[ItemsTableRow] = self.__items_crud.find_all_by_ids([id.value for id in ids])
        return [self.__generate_item_from(row) for row in table_rows]

    def upsert(self, item: Item):
        self.__items_crud.upsert(self.__to_items_table_row(item))

    def delete(self, id: ItemId):
        self.__items_crud.delete(id.value)

    @staticmethod
    def __generate_item_from(items_table_row: ItemsTableRow) -> Item:
        return Item(
            ItemId(items_table_row.id),
            ItemName(items_table_row.name),
            BrandName(items_table_row.brand_name),
            Price(items_table_row.price, Price.Currency.yen),
            Gender[items_table_row.gender],
            ItemImageList([ItemImage(URL(image_url)) for image_url in eval(items_table_row.images)]),
            URL(items_table_row.url)
        )

    @staticmethod
    def __to_items_table_row(item: Item) -> ItemsTableRow:
        return ItemsTableRow(id=item.id.value,
                             brand_name=item.brand_name.text,
                             name=item.name.text,
                             price=item.price.type_of(Price.PriceType.NORMAL_PRICE).amount,
                             images="{}".format([image.url.address for image in item.images.list]),
                             gender=item.gender.name,
                             url=item.url.address,
                             meta_keywords=item.meta.name_of(Meta.MetaName.keywords).value,
                             meta_description=item.meta.name_of(Meta.MetaName.description).value,
                             meta_content=item.meta.name_of(Meta.MetaName.content).value)
