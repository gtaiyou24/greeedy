from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class ItemId:
    value: str

    def __init__(self, id: str):
        assert isinstance(id, str), "idには文字列を指定して下さい"
        id = id.strip()  # 前後の空文字を削除
        assert id, "idは必須です"
        super().__setattr__("value", id)
