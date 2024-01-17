import json

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

    def to_json_str(self) -> str:
        d = {
            "char": self.char,
            "pinyin": self.pinyin,
            "definition": self.definition,
            "stroke_count": self.stroke_count,
        }
        return json.dumps(d)

    @staticmethod
    def from_json_str(json_str: str) -> Union["Character", None]:
        try:
            json_dict = json.loads(json_str)
            return Character(
                char=json_dict["char"],
                pinyin=json_dict["pinyin"],
                definition=json_dict["definition"],
                stroke_count=json_dict["stroke_count"],
            )
        except Exception as e:
            print(f"[character] error reading {json_str} into Character: {e}")
            return None
