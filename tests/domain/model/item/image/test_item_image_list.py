from typing import NoReturn

import pytest

from domain.model.color import Color
from domain.model.item.image import ItemImageList, ItemImage, ImageType
from domain.model.url import URL


class TestItemImageList:
    class Test_生成について:
        def test_アイテム画像のリスト指定で生成できる(self) -> NoReturn:
            try:
                ItemImageList([
                    ItemImage(ImageType.MODEL_WEARING, Color.RED, URL('http://example.jp/images/1.jpg')),
                    ItemImage(ImageType.ONLY_ITEM, Color.RED, URL('http://example.jp/images/2.jpg')),
                    ItemImage(ImageType.ZOOM_IN, Color.RED, URL('http://example.jp/images/3.jpg')),
                ])
            except Exception:
                pytest.fail('This code should be executed.')

        @pytest.mark.parametrize("arg", [None, []])
        def test_空のリストもしくはNoneを指定するとAssertionErrorを送出する(self, arg) -> NoReturn:
            with pytest.raises(AssertionError):
                ItemImageList(arg)

        def test_アイテム画像を要素としたList型以外を指定するとAssertionErrorを送出する(self) -> NoReturn:
            with pytest.raises(AssertionError):
                ItemImageList({ItemImage(ImageType.MODEL_WEARING, Color.RED, URL('http://example.jp/images/1.jpg')),
                               ItemImage(ImageType.ONLY_ITEM, Color.RED, URL('http://example.jp/images/2.jpg')),
                               ItemImage(ImageType.ZOOM_IN, Color.RED, URL('http://example.jp/images/3.jpg'))})

        def test_重複したアイテム画像を指定するとAssertionErrorを送出する(self) -> NoReturn:
            with pytest.raises(AssertionError):
                ItemImageList([
                    ItemImage(ImageType.MODEL_WEARING, Color.RED, URL('http://example.jp/images/1.jpg')),
                    ItemImage(ImageType.MODEL_WEARING, Color.RED, URL('http://example.jp/images/1.jpg')),
                    ItemImage(ImageType.ONLY_ITEM, Color.RED, URL('http://example.jp/images/2.jpg')),
                ])

    class Test_sortメソッドについて:
        def test_アイテム画像のリストのうち先頭にあるズームイン画像を末尾に並び替えて再生成する(self) -> NoReturn:
            model_wearing = ItemImage(ImageType.MODEL_WEARING, Color.RED, URL('http://example.jp/images/1.jpg'))
            only_item = ItemImage(ImageType.ONLY_ITEM, Color.RED, URL('http://example.jp/images/2.jpg'))
            zoom_in = ItemImage(ImageType.ZOOM_IN, Color.RED, URL('http://example.jp/images/3.jpg'))
            top_zoom_in = ItemImage(ImageType.ZOOM_IN, Color.RED, URL('http://example.jp/images/4.jpg'))

            item_image_list = ItemImageList([top_zoom_in, model_wearing, only_item, zoom_in])

            assert item_image_list.sort() == ItemImageList([model_wearing, only_item, zoom_in, top_zoom_in])

        def test_ズームイン画像しかないアイテム画像リストは並び替えしないで再生成する(self) -> NoReturn:
            item_image_list = ItemImageList([
                ItemImage(ImageType.ZOOM_IN, Color.BLACK, URL('http://example.jp/images/1.jpg')),
                ItemImage(ImageType.ZOOM_IN, Color.BLACK, URL('http://example.jp/images/2.jpg')),
                ItemImage(ImageType.ZOOM_IN, Color.BLACK, URL('http://example.jp/images/3.jpg')),
            ])
            assert item_image_list.sort() == item_image_list
