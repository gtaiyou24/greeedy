from typing import Optional

from domain.model import DomainEventPublisher, DomainEventSubscriber, DomainEvent


class ApplicationServiceLifeCycle:
    event_store = []

    @staticmethod
    def begin(is_listening: bool = True):
        if is_listening:
            ApplicationServiceLifeCycle.listen()
        # TODO : トランザクションスタート

    @staticmethod
    def fail(exception: Optional[Exception] = None):
        # TODO : ロールバック実行
        if exception is not None:
            raise exception

    @staticmethod
    def success():
        # コミットする
        pass

    @staticmethod
    def listen():
        class DomainEventSubscriberImpl(DomainEventSubscriber):
            event_store = []

            def handle_event(self, domain_event: DomainEvent):
                self.event_store.append(domain_event)

            def subscribed_to_event_type(self) -> type:
                # 全てのドメインイベント
                return DomainEvent.__class__

        DomainEventPublisher.shared().reset()
        DomainEventPublisher.shared().subscribe(DomainEventSubscriberImpl[DomainEvent]())
