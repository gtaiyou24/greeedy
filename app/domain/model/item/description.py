from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Description:
    text: str

    def __init__(self, text: str):
        assert isinstance(text, str), "説明文には文字列を指定して下さい"
        super().__setattr__("text", text)
