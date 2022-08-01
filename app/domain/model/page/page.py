from dataclasses import dataclass

from domain.model.url import URL


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Page:
    url: URL
    keywords: str
    description: str

    def __init__(self, url: URL, keywords: str, description: str):
        assert isinstance(url, URL), 'URLは必須です。'
        assert isinstance(keywords, str), 'keywordsには文字列を指定してください。'
        assert isinstance(description, str), 'descriptionには文字列を指定してください。'
        super().__setattr__("url", url)
        super().__setattr__("keywords", keywords)
        super().__setattr__("description", description)
