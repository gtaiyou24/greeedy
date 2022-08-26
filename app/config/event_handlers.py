from typing import NoReturn

from di import DIManager
from port.adapter.messaging.sqs import SQSMessageConsumer


message_consumer = DIManager.get(SQSMessageConsumer)


async def startup_handler() -> NoReturn:
    # TODO : DIさせる
    # TODO : NotificationPublisherTimer.start()
    message_consumer.start_receiving()


async def shutdown_handler() -> NoReturn:
    message_consumer.stop_receiving()
