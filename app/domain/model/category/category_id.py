import re
from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class CategoryId:
    __VALIDATION_REGEX = re.compile(r'[0-9A-Za-z-]+')
    value: str

    def __init__(self, value: str):
        assert isinstance(value, str), "カテゴリIDには文字列を指定して下さい。"
        value = value.strip()
        assert value, "カテゴリIDは必須です。"
        assert self.__VALIDATION_REGEX.match(value), "カテゴリIDには大文字小文字の英数字と-(ハイフン)を指定してください。(arg={})".format(value)
        super().__setattr__("value", value)
