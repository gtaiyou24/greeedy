import abc
from typing import NoReturn


from exception import SystemException
from port.adapter.messaging import ExchangeListener


class MessageConsumer(abc.ABC):
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

    @abc.abstractmethod
    def exchange_listeners(self) -> list[ExchangeListener]:
        pass

    @abc.abstractmethod
    def __producer_name_of(self, message: str) -> str:
        pass

    @abc.abstractmethod
    def __event_type_of(self, message: str) -> str:
        pass

    @abc.abstractmethod
    def __body_of(self, message: str) -> str:
        pass
