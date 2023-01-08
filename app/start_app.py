from fastapi import FastAPI
from mangum import Mangum
from mangum.types import LambdaEvent, LambdaContext

from core import exception_handlers, event_handlers
from exception import SystemException
from port.adapter.messaging.sqs import SQSMessageConsumer
from port.adapter.resource.category import category_resource
from port.adapter.resource.health import health_resource
from port.adapter.resource.item import item_resource


app = FastAPI(title="Greeedy")

app.add_exception_handler(SystemException, exception_handlers.system_exception_handler)

app.add_event_handler('startup', event_handlers.startup_handler)
app.add_event_handler('shutdown', event_handlers.shutdown_handler)

app.include_router(category_resource.router)
app.include_router(health_resource.router)
app.include_router(item_resource.router)


def handler(event: LambdaEvent, context: LambdaContext):
    # トリガーがMQの場合
    if 'Records' in event:
        message_consumer = SQSMessageConsumer()
        for record in event['Records']:
            message_consumer.dispatch_message(record['body'])
        return

    # トリガーがAPI Gatewayの場合
    asgi_handler = Mangum(app, lifespan="off")
    return asgi_handler(event, context)
