import json


class ChengYu:
    chars: str
    pinyin: str
    definition: str
    source: str
    example: str

    def __init__(
        self, chars: str, pinyin: str, definition: str, source: str, example: str
    ):
        self.chars = chars
        self.pinyin = pinyin
        self.definition = definition
        self.source = source
        self.example = example

    def __str__(self) -> str:
        return f"{self.chars} ({self.pinyin}): {self.definition} source={self.source} ({self.example})"

    def __repr__(self) -> str:
        return str(self)

    def to_json_str(self) -> str:
        d = {
            "chars": self.chars,
            "pinyin": self.pinyin,
            "definition": self.definition,
            "source": self.source,
            "example": self.example,
        }
        return json.dumps(d)

    @staticmethod
    def from_json_str(json_str: str) -> "ChengYu":
        try:
            json_dict = json.loads(json_str)
            return ChengYu(
                chars=json_dict["chars"],
                pinyin=json_dict["pinyin"],
                definition=json_dict["definition"],
                source=json_dict["source"],
                example=json_dict["example"],
            )
        except Exception as e:
            print(f"[ChengYu] error reading {json_str} into ChengYu: {e}")
            return None
