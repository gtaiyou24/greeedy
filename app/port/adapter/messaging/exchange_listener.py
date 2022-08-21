import abc
from enum import Enum
from typing import NoReturn


class ExchangeListener(abc.ABC):
    class ProducerName(Enum):
        EPIC_BOT_PRODUCER_NAME = 'epic-bot'

    def __init__(self, producer_name: ProducerName, event_types: set[str]):
        assert producer_name, "購読するイベント発行元コンテキストを指定してください。"
        assert event_types, "購読するイベントタイプの一覧は必須です。"
        self.__producer_name = producer_name.value
        self.__event_types = event_types

    @abc.abstractmethod
    def filtered_dispatch(self, event_type: str, text_message: str) -> NoReturn:
        """イベントタイプとメッセージ指定でメッセージを処理する"""
        pass

    @property
    def producer_name(self) -> str:
        return self.__producer_name

    def listens_to(self, event_type: str) -> bool:
        """イベントタイプ指定で購読するイベントかどうかを判定する"""
        return event_type in self.__event_types
