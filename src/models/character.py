from typing import Union


class Character:
    char: str
    pinyin: Union[str, None]
    definition: Union[str, None]
    stroke_count: int

    def __init__(
        self,
        char: str,
        pinyin: Union[str, None],
        definition: Union[str, None],
        stroke_count: int,
    ):
        self.char = char
        self.pinyin = pinyin if pinyin else None
        self.definition = definition if definition else None
        self.stroke_count = stroke_count

    def __str__(self) -> str:
        return f"{self.char} ({self.pinyin}, {self.stroke_count}): {self.definition}"

    def __repr__(self) -> str:
        return str(self)
