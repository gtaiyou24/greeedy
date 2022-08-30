import json
import threading
import time
from typing import NoReturn

from injector import inject, singleton
from slf4py import set_logger

from di import DIManager
from exception import SystemException
from port.adapter.messaging import ItemCreatedListener
from port.adapter.messaging.sqs import SQSClient


@set_logger
@singleton
class SQSMessageConsumer:
    @inject
    def __init__(self, sqs_client: SQSClient):
        self.__exchange_listeners = [
            DIManager.get(ItemCreatedListener)
        ]
        self.__sqs_client = sqs_client
        self.__is_running = True

    def start_receiving(self) -> NoReturn:
        self.log.info('start receiving message!')

        def run() -> NoReturn:
            while self.__is_running:
                self.log.info('receive message ...')
                messages = self.__sqs_client.receive_messages()
                if messages:
                    self.log.info('dispatch message!')
                    for message in messages:
                        self.dispatch_message(message['Body'])
                        self.__sqs_client.delete_message(message)
                        self.log.info('message is subscribed!')
                else:
                    self.log.info('no message')
                    time.sleep(5)

        receiver_thread = threading.Thread(target=run)
        receiver_thread.start()

    def stop_receiving(self) -> NoReturn:
        self.log.info('stop receiving')
        self.__is_running = False

    def dispatch_message(self, message: str) -> NoReturn:
        producer_name = self.__producer_name_of(message)
        event_type = self.__event_type_of(message)
        event = self.__event_of(message)

        for listener in self.__exchange_listeners:
            if listener.producer_name == producer_name and listener.listens_to(event_type):
                try:
                    listener.filtered_dispatch(event_type, event)
                except SystemException as e:
                    e.logging()

    def __producer_name_of(self, message: str) -> str:
        return eval(message)['producer_name']

    def __event_type_of(self, message: str) -> str:
        return eval(message)['event_type']

    def __event_of(self, message: str) -> str:
        return json.dumps(eval(message)['event'])
