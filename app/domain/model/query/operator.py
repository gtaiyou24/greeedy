from __future__ import annotations

from enum import Enum


class Operator(Enum):
    AND = "and"
    OR = "or"
    NOT = "not"

    @staticmethod
    def value_of(name: str) -> Operator:
        for e in Operator:
            if e.value == name:
                return e
        raise ValueError(f'{name} に合致するOperatorクラスは存在しません。')
