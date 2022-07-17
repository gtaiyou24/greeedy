from dataclasses import dataclass


@dataclass(init=False, frozen=True, unsafe_hash=True)
class BrandName:
    text: str

    def __init__(self, name: str):
        assert isinstance(name, str), "ブランド名には文字列を指定して下さい"

        name = name.strip()
        assert name, "ブランド名は必須です"

        super().__setattr__("text", name)
