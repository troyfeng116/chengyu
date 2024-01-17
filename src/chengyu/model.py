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
