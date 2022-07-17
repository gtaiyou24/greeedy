import re
from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class CategoryName:
    __NAME_REGEX = re.compile(r'\S')
    text: str

    def __init__(self, text: str):
        assert isinstance(text, str), "カテゴリ名には文字列を指定して下さい"
        text = text.strip()
        assert text, "カテゴリ名は必須です"
        assert re.match(r'', text), "カテゴリ名"
        assert self.__NAME_REGEX.match(text), "カテゴリ名には空白文字列以外を指定して下さい"
        super().__setattr__("text", text)
