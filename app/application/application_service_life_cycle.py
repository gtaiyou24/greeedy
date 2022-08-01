from typing import Optional

from injector import singleton, inject

from config import MySQLConfig
from domain.model import DomainEventPublisher, DomainEventSubscriber, DomainEvent


@singleton
class ApplicationServiceLifeCycle:
    @inject
    def __init__(self, mysql_config: MySQLConfig):
        self.__session = mysql_config.session()

    def begin(self, is_listening: bool = True):
        if is_listening:
            self.listen()
        self.__session.begin()

    def fail(self, exception: Optional[Exception] = None):
        self.__session.rollback()
        if exception is not None:
            raise exception

    def success(self):
        self.__session.commit()

    def listen(self):
        class DomainEventSubscriberImpl(DomainEventSubscriber):
            event_store = []

            def handle_event(self, domain_event: DomainEvent):
                self.event_store.append(domain_event)

            def subscribed_to_event_type(self) -> type:
                # 全てのドメインイベント
                return DomainEvent.__class__

        DomainEventPublisher.shared().reset()
        DomainEventPublisher.shared().subscribe(DomainEventSubscriberImpl[DomainEvent]())
