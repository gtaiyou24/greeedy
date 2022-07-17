from typing import Optional, Set

from injector import inject

from config import ElasticsearchConfig
from domain.model.gender import Gender
from domain.model.item import ItemIndex, Item, SearchHitItems, Price
from domain.model.item.id import ItemId
from domain.model.item.meta import Meta


class ElasticsearchItemIndex(ItemIndex):
    INDEX_NAME = "items_20220224"

    @inject
    def __init__(self, config: ElasticsearchConfig):
        self.__config = config
        self.__search_engine = self.__config.engine()

    def add(self, item: Item):
        document = {
            'name': item.name.text,
            'brand_name': item.brand_name.text,
            'price': item.price.type_of(Price.PriceType.NORMAL_PRICE).amount,
            'gender': item.gender.name,
            'images': [image.url.address for image in item.images.list],
            'page_url': item.url.address,
            'keywords': item.meta.name_of(Meta.MetaName.keywords).value,
            'description': item.meta.name_of(Meta.MetaName.description).value,
            'content': item.meta.name_of(Meta.MetaName.content).value,
        }
        self.__search_engine.index(index=self.INDEX_NAME, id=item.id.value, body=document)

    def delete(self, item_id: ItemId):
        self.__search_engine.delete(index=self.INDEX_NAME, id=item_id.value)

    def search(self, gender: Gender, text: Optional[str],
               category: Optional[str], colors: Set[str],
               designs: Set[str], details: Set[str],
               price_from: Optional[int], price_to: Optional[int],
               sort: str, start: int, size: int) -> SearchHitItems:
        pass
