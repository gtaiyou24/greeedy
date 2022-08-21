from __future__ import annotations

from enum import Enum


class Color(Enum):
    WHITE = 'white'
    BLACK = 'black'
    GRAY = 'gray'
    BROWN = 'brown'
    BEIGE = 'beige'
    GREEN = 'green'
    BLUE = 'blue'
    PURPLE = 'purple'
    YELLOW = 'yellow'
    PINK = 'pink'
    RED = 'red'
    ORANGE = 'orange'
    OTHER = 'other'
    UNKNOWN = 'unknown'

    @classmethod
    def value_of(cls, a_value: str) -> Color:
        for e in cls:
            if e.value == a_value:
                return e
        raise ValueError("{} はColorに定義されていません".format(a_value))
