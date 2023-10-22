import os
from typing import NoReturn

import requests
from di import DIContainer, DI
from requests.adapters import HTTPAdapter
from sqlalchemy.orm import Session
from urllib3 import Retry

from core import MySQLConfig
from domain.model.category import CategoryRepository
from domain.model.item import ItemIndex, ItemRepository
from domain.model.item.id import ItemIdFactoryImpl, ItemIdFactory
from domain.model.item.image import ItemImageService, ItemImageStorageService
from port.adapter.messaging.sqs import SQSMessageConsumer
from port.adapter.persistence.index.elasticsearch.item import ElasticsearchItemIndex
from port.adapter.persistence.repository.mysql import Base
from port.adapter.persistence.repository.mysql.category import MySQLCategoryRepository
from port.adapter.persistence.repository.mysql.item import MySQLItemRepository
from port.adapter.service.item.image import ItemImageServiceImpl, ItemImageStorageServiceImpl
from port.adapter.service.item.image.adapter import ColorAdapter, ImageTypeAdapter, ImageStorageAdapter
from port.adapter.service.item.image.adapter.huggingface import FashionImagesPerspectivesAdapter, FashionCLIPAdapter
from port.adapter.service.item.image.adapter.s3 import ImageS3Adapter
from port.adapter.standalone.adapterstub import ColorAdapterStub
from port.adapter.standalone.inmemory import InMemCategoryRepository, InMemItemRepository


async def startup_handler() -> NoReturn:
    # register DI to injector
    DIContainer.instance().register(DI.of(ItemIndex, {}, ElasticsearchItemIndex))
    DIContainer.instance().register(DI.of(ItemRepository,
                                          {'inmemory': InMemItemRepository, 'mysql': MySQLItemRepository},
                                          MySQLItemRepository))
    DIContainer.instance().register(DI.of(ItemIdFactory, {}, ItemIdFactoryImpl))
    DIContainer.instance().register(DI.of(ItemImageService, {}, ItemImageServiceImpl))
    DIContainer.instance().register(DI.of(ItemImageStorageService, {}, ItemImageStorageServiceImpl))
    DIContainer.instance().register(DI.of(ColorAdapter, {'adapterstub': ColorAdapterStub}, FashionCLIPAdapter))
    DIContainer.instance().register(DI.of(ImageStorageAdapter, {}, ImageS3Adapter))
    DIContainer.instance().register(DI.of(ImageTypeAdapter, {}, FashionImagesPerspectivesAdapter(os.getenv('HUGGING_FACE_API_TOKEN'))))
    DIContainer.instance().register(DI.of(CategoryRepository,
                                          {'inmemory': InMemCategoryRepository, 'mysql': MySQLCategoryRepository},
                                          MySQLCategoryRepository))

    session = requests.Session()
    retries = Retry(total=3,  # リトライ回数
                    backoff_factor=2,  # sleep時間
                    status_forcelist=[500, 502, 503, 504])  # timeout以外でリトライするステータスコード
    session.mount("https://", HTTPAdapter(max_retries=retries))
    DIContainer.instance().register(DI.of(requests.Session, {}, session))

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
