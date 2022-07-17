from __future__ import annotations

from dataclasses import dataclass

from domain.model.gender import Gender
from domain.model.item import ItemName, BrandName, Price
from domain.model.item.id import ItemId
from domain.model.item.image import ItemImageList
from domain.model.item.meta import Meta
from domain.model.url import URL


@dataclass(init=False, eq=False, unsafe_hash=True)
class Item:
    id: ItemId
    name: ItemName
    brand_name: BrandName
    price: Price
    gender: Gender
    images: ItemImageList
    url: URL
    meta: Meta

    def __init__(self, id: ItemId, name: ItemName, brand_name: BrandName, price: Price,
                 gender: Gender, images: ItemImageList, url: URL, meta: Meta):
        assert isinstance(id, ItemId), "IDにはItemIdを指定してください(type={})".format(type(id))
        assert isinstance(name, ItemName), "アイテム名にはItemNameを指定してください(type={})".format(type(name))
        assert isinstance(brand_name, BrandName), "ブランド名にはBrandNameを指定してください(type={})".format(type(brand_name))
        assert isinstance(price, Price), "価格にはPriceを指定してください(type={})".format(type(brand_name))
        assert isinstance(gender, Gender), "性別にはGenderを指定してください(type={})".format(type(gender))
        assert isinstance(images, ItemImageList), "画像一覧にはItemImageListを指定してください(type={})".format(type(images))
        assert isinstance(url, URL), "ページURLにはURLを指定してください(type={})".format(type(url))
        assert isinstance(meta, Meta), "メタ情報にはMetaを指定してください(type={})".format(type(meta))
        super().__setattr__("id", id)
        super().__setattr__("name", name)
        super().__setattr__("brand_name", brand_name)
        super().__setattr__("price", price)
        super().__setattr__("gender", gender)
        super().__setattr__("images", images)
        super().__setattr__("url", url)
        super().__setattr__("meta", meta)

    def __eq__(self, other: Item):
        if not isinstance(other, Item) or other is None:
            return False
        return self.id == other.id
