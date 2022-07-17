from dataclasses import dataclass


@dataclass(init=False, frozen=True, unsafe_hash=True)
class ItemName:
    text: str

    def __init__(self, text: str):
        assert isinstance(text, str), "アイテム名には文字列を指定して下さい"

        text = text.strip()
        assert text, "アイテム名は必須です"

        super().__setattr__("text", text)
