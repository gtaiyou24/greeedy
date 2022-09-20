from typing import Optional

from injector import singleton
from slf4py import set_logger

from config.db import session
from domain.model import DomainEventPublisher, DomainEventSubscriber, DomainEvent


@set_logger
@singleton
class ApplicationServiceLifeCycle:
    def __init__(self):
        self.__session = session

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
        self.log.debug('session committed')

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
