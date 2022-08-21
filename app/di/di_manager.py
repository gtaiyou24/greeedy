from typing import Type

from injector import Injector, T

from di import DI
from domain.model.category import CategoryRepository
from domain.model.item import ItemIndex, ItemRepository
from domain.model.item.id import ItemIdFactory, ItemIdFactoryImpl
from domain.model.item.image import ItemImageService
from port.adapter.persistence.index.elasticsearch.item import ElasticsearchItemIndex
from port.adapter.persistence.repository.inmemory import InMemoryItemRepository, InMemCategoryRepository
from port.adapter.persistence.repository.mysql.item import MySQLItemRepository
from port.adapter.service.item.image import ItemImageServiceImpl
from port.adapter.service.item.image.adapter import ItemImageAdapter
from port.adapter.service.item.image.adapter.greeedyml import GreeedyMLItemImageAdapter


class DIManager:
    __injector = Injector([
        DI.new(ItemIndex, {}, ElasticsearchItemIndex),
        DI.new(ItemRepository, {"inmemory": InMemoryItemRepository, "mysql": MySQLItemRepository}, InMemoryItemRepository),
        DI.new(ItemIdFactory, {}, ItemIdFactoryImpl),
        DI.new(ItemImageService, {}, ItemImageServiceImpl),
        DI.new(ItemImageAdapter, {}, GreeedyMLItemImageAdapter),
        DI.new(CategoryRepository, {}, InMemCategoryRepository),
    ])

    @classmethod
    def get(cls, interface: Type[T]) -> T:
        return cls.__injector.get(interface)
