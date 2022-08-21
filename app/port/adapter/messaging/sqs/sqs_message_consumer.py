import json
from typing import NoReturn

from di import DIManager
from exception import SystemException
from port.adapter.messaging import ItemCreatedListener, ExchangeListener, MessageConsumer


class SQSMessageConsumer:
    def __init__(self):
        self.__exchange_listeners = [
            DIManager.get(ItemCreatedListener)
        ]

    def dispatch_message(self, message: str) -> NoReturn:
        producer_name = self.__producer_name_of(message)
        event_type = self.__event_type_of(message)
        body = self.__body_of(message)

        for listener in self.exchange_listeners():
            if listener.producer_name == producer_name and listener.listens_to(event_type):
                try:
                    listener.filtered_dispatch(event_type, body)
                except SystemException as e:
                    e.logging()

    def exchange_listeners(self) -> list[ExchangeListener]:
        return self.__exchange_listeners

    def __producer_name_of(self, message: str) -> str:
        return eval(message)['producer_name']

    def __event_type_of(self, message: str) -> str:
        return eval(message)['event_type']

    def __body_of(self, message: str) -> str:
        return json.dumps(eval(message)['body'])
