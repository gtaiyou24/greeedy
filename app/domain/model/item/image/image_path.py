import re
from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class ImagePath:
    file_path: str

    def __init__(self, file_path: str):
        assert file_path, "ファイルパスは必須です。"
        assert re.match(r'^/.+\.(jpeg|jpg|png|bmp|gif|webp)$', file_path), "画像ファイルを絶対パスで指定してください。"
        super().__setattr__("file_path", file_path)
