from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class URL:
    __ABSOLUTE_URL_REGEX = re.compile(r"^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+")
    address: str

    def __init__(self, url: str):
        assert url, "URLは必須です。"
        assert isinstance(url, str), "URLに{}が指定されています。文字列を指定して下さい。".format(type(url))
        assert self.__ABSOLUTE_URL_REGEX.match(url), "{}は完全URLではありません。完全URLを指定して下さい。".format(URL)
        super().__setattr__("address", url)
