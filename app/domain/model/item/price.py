from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass(init=False, unsafe_hash=True, frozen=False)
class Price:
    amount: float
    currency: Currency
    type: PriceType
    other_price: Optional[Price]

    class PriceType(Enum):
        NORMAL_PRICE = "通常価格"
        DISCOUNT_PRICE = "割引価格"
        MEMBER_PRICE = "会員価格"

    class Currency(Enum):
        JPY = "日本円"
        USD = "米ドル"

    def __init__(self, amount: float, currency: Price.Currency, type: PriceType = PriceType.NORMAL_PRICE):
        assert (isinstance(amount, float) or isinstance(amount, int)) and amount >= 0, \
            "amountには0以上のfloat/int型を指定してください。"
        assert isinstance(currency, Price.Currency), "currencyにはPrice.Currency型を指定してください。"
        assert isinstance(type, Price.PriceType), "typeにはPrice.PriceType型を指定してください。"
        super().__setattr__("amount", amount)
        super().__setattr__("currency", currency)
        super().__setattr__("type", type)
        super().__setattr__("other_price", None)

    def set_other_price(self, price: Price) -> Price:
        self.other_price = price
        return self.other_price

    def type_of(self, price_type: PriceType) -> Optional[Price]:
        if self.type == price_type:
            return self

        if self.other_price is not None:
            return self.other_price.type_of(price_type)

        return None
