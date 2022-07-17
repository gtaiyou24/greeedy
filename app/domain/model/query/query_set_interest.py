import abc
from typing import TypeVar, Generic

from domain.model.query import QuerySet

T = TypeVar('T')


class QuerySetInterest(abc.ABC, Generic[T]):
    @abc.abstractmethod
    def to_payload_from(self, query_set: QuerySet) -> T:
        pass

    @abc.abstractmethod
    def to_query_from(self, payload: T) -> QuerySet:
        pass
