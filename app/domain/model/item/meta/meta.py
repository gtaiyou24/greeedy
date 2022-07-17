from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass(init=False, unsafe_hash=True, frozen=False)
class Meta:
    name: MetaName
    value: str
    other_meta: Optional[Meta]

    class MetaName(Enum):
        description = "説明文"
        keywords = "キーワード"
        content = "コンテンツ"

    def __init__(self, name: MetaName, value: str):
        assert isinstance(name, Meta.MetaName), "メタ名は必須です"
        assert isinstance(value, str), "メタデータには文字列を指定してください"
        value = value.strip()
        assert value, "メタデータは必須です"
        super().__setattr__("name", name)
        super().__setattr__("value", value)
        super().__setattr__("other_meta", None)

    def set_other_meta(self, other_meta: Meta):
        if self.other_meta is None:
            self.other_meta = other_meta
        else:
            self.other_meta.set_other_meta(other_meta)

    def name_of(self, name: MetaName) -> Optional[Meta]:
        if self.name == name:
            return self

        if self.other_meta is not None:
            return self.other_meta.name_of(name)

        return None
