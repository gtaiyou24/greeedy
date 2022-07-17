from dataclasses import dataclass
from typing import Set

from domain.model.query import Query, Operator


@dataclass(init=False, unsafe_hash=True, frozen=True)
class QuerySet:
    all: dict[Operator:Set[Query]]

    def __init__(self, all: dict[Operator:Set[Query]]):
        super().__setattr__("all", all)

    def queries_of(self, operator: Operator) -> Set[Query]:
        return self.all[operator]

    def operators(self) -> Set[Operator]:
        return set(self.all.keys())
