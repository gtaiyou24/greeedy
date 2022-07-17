from __future__ import annotations

from dataclasses import dataclass

from domain.model.query import Operator


@dataclass(init=False, unsafe_hash=True, frozen=True)
class Query:
    text: str
    operator: Operator

    def __init__(self, text: str, operator: Operator = Operator.AND):
        super().__setattr__("text", text)
        super().__setattr__("operator", operator)

    def is_empty(self) -> bool:
        return self.text == ""
