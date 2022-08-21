from typing import NoReturn

from injector import inject
from slf4py import set_logger

from application.item.command import ProcessItemCommand
from application.item.service import ProcessItemApplicationService
from notification import NotificationReader
from port.adapter.messaging import ExchangeListener


@set_logger
class ItemCreatedListener(ExchangeListener):
    @inject
    def __init__(self, process_item_application: ProcessItemApplicationService):
        super(ItemCreatedListener, self).__init__(
            producer_name=ExchangeListener.ProducerName.EPIC_BOT_PRODUCER_NAME,
            event_types={'epic-scraper.ItemCreated.1'}
        )
        self.__process_item_application = process_item_application

    def filtered_dispatch(self, event_type: str, text_message: str) -> NoReturn:
        self.log.debug(f'event_type = {event_type}, text_message = {text_message}')
        reader = NotificationReader(text_message)

        self.__process_item_application.process(
            ProcessItemCommand(
                name=reader.event_str_value('name'),
                brand_name=reader.event_str_value('brand_name'),
                price=reader.event_float_value('price'),
                description=reader.event_str_value('description'),
                gender=reader.event_str_value('gender'),
                images=[ProcessItemCommand.Image(url=image) for image in eval(reader.event_str_value('images'))],
                url=reader.event_str_value('url'),
                meta=ProcessItemCommand.Meta(
                    keywords=reader.event_str_value('meta.keywords'),
                    description=reader.event_str_value('meta.description')
                )
            )
        )
