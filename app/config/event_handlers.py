import os
from typing import NoReturn

from di import DIContainer, DI
from sqlalchemy.orm import Session

from config import MySQLConfig
from domain.model.category import CategoryRepository
from domain.model.item import ItemIndex, ItemRepository
from domain.model.item.id import ItemIdFactoryImpl, ItemIdFactory
from domain.model.item.image import ItemImageService
from port.adapter.messaging.sqs import SQSMessageConsumer
from port.adapter.persistence.index.elasticsearch.item import ElasticsearchItemIndex
from port.adapter.persistence.repository.mysql import Base
from port.adapter.persistence.repository.mysql.category import MySQLCategoryRepository
from port.adapter.persistence.repository.mysql.item import MySQLItemRepository
from port.adapter.service.item.image import ItemImageServiceImpl
from port.adapter.service.item.image.adapter import ItemImageAdapter
from port.adapter.service.item.image.adapter.greeedyml import GreeedyMLItemImageAdapter
from port.adapter.standalone.inmemory import InMemCategoryRepository, InMemItemRepository


async def startup_handler() -> NoReturn:
    # register DI to injector
    DIContainer.instance().register(DI.of(ItemIndex, {}, ElasticsearchItemIndex))
    DIContainer.instance().register(DI.of(ItemRepository,
                                          {'inmemory': InMemItemRepository, 'mysql': MySQLItemRepository},
                                          MySQLItemRepository))
    DIContainer.instance().register(DI.of(ItemIdFactory, {}, ItemIdFactoryImpl))
    DIContainer.instance().register(DI.of(ItemImageService, {}, ItemImageServiceImpl))
    DIContainer.instance().register(DI.of(ItemImageAdapter, {}, GreeedyMLItemImageAdapter))
    DIContainer.instance().register(DI.of(CategoryRepository,
                                          {'inmemory': InMemCategoryRepository, 'mysql': MySQLCategoryRepository},
                                          MySQLCategoryRepository))
    # run consumer thread
    message_consumer = DIContainer.instance().resolve(SQSMessageConsumer)
    message_consumer.start_receiving()
    # for mysql
    if 'mysql' in os.environ.get('DI_PROFILE_ACTIVES'):
        config = DIContainer.instance().resolve(MySQLConfig)
        DIContainer.instance().register(
            DI.of(Session, {}, Session(autocommit=False, autoflush=False, bind=config.engine())))
        Base.metadata.create_all(bind=config.engine())


async def shutdown_handler() -> NoReturn:
    message_consumer = DIContainer.instance().resolve(SQSMessageConsumer)
    message_consumer.stop_receiving()
