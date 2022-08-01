from typing import Optional, Set, NoReturn

from elasticsearch_dsl import Search, Index
from elasticsearch_dsl.response import Response
from injector import inject

from config import ElasticsearchConfig
from domain.model.category import Category
from domain.model.color import Color
from domain.model.gender import Gender
from domain.model.item import ItemIndex, Item, SearchHitItems, Price, ItemName, BrandName, Description
from domain.model.item.id import ItemId
from domain.model.item.image import ItemImageList, ItemImage, ImageType
from domain.model.page import Page
from domain.model.url import URL
from port.adapter.persistence.index.elasticsearch.item import ItemIndexRow, ItemQueryBuilder


class ElasticsearchItemIndex(ItemIndex):
    @inject
    def __init__(self, config: ElasticsearchConfig):
        self.__search_engine = config.engine()
        Index(ItemIndexRow.Index.name, using=self.__search_engine).close()
        ItemIndexRow.init(using=self.__search_engine)
        Index(ItemIndexRow.Index.name, using=self.__search_engine).open()

    def add(self, item: Item) -> NoReturn:
        item_index_row = ItemIndexRow(
            meta={'id': item.id.value},
            name=item.name.text,
            brand_name=item.brand_name.text,
            price=item.price.type_of(Price.PriceType.NORMAL_PRICE).amount,
            description=item.description.text,
            gender=item.gender.name,
            images=[{"type": image.type.name, "color": image.color.name, "url": image.url.address} \
                    for image in item.images.list],
            page={
                "keywords": item.page.keywords,
                "description": item.page.description,
                "url": item.page.url.address
            }
        )
        item_index_row.save(using=self.__search_engine)

    def get(self, item_id: ItemId) -> Optional[Item]:
        item_document = ItemIndexRow.get(item_id.value, using=self.__search_engine)
        if item_document is None:
            return None

        return Item(
            ItemId(str(item_document.meta.id)),
            ItemName(str(item_document.name)),
            BrandName(str(item_document.brand_name)),
            Price(int(item_document.price), Price.Currency.JPY),
            Description(str(item_document.description)),
            Gender[str(item_document.gender)],
            ItemImageList([ItemImage(ImageType[image.type], Color[image.color], URL(image.url)) \
                           for image in item_document.images]),
            Page(
                URL(str(item_document.page.url)),
                str(item_document.page.keywords),
                str(item_document.page.description)
            )
        )

    def delete(self, item_id: ItemId) -> NoReturn:
        self.__search_engine.delete(index=ItemIndexRow.Index.name, id=item_id.value)

    def search(self, gender: Gender, text: Optional[str],
               category: Optional[Category], colors: Set[Color],
               designs: Set[str], details: Set[str],
               price_from: Optional[int], price_to: Optional[int],
               sort: str = "relevance", start: int = 1, size: int = 20) -> SearchHitItems:
        query = ItemQueryBuilder()\
            .gender(gender)\
            .text(text)\
            .category(category)\
            .colors(colors)\
            .designs(designs)\
            .details(details)\
            .price(price_from, price_to)\
            .build()

        response: Response = Search(using=self.__search_engine, index=ItemIndexRow.Index.name)\
            .query(query).extra(from_=start-1, size=size).execute()

        items = []
        for hit in response.hits:
            item = Item(
                ItemId(str(hit.meta.id)),
                ItemName(str(hit.name)),
                BrandName(str(hit.brand_name)),
                Price(int(hit.price), Price.Currency.JPY),
                Description(str(hit.description)),
                Gender[str(hit.gender)],
                ItemImageList([ItemImage(ImageType[image.type], Color[image.color], URL(image.url)) \
                               for image in hit.images]),
                Page(URL(str(hit.page.url)), str(hit.page.keywords), str(hit.page.description))
            )
            items.append(item)
        return SearchHitItems(int(response.hits.total.value), items)
