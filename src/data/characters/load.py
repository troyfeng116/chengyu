from typing import List

from src.models.character import Character
from src.data.characters.fetch_and_store import CHARS_FILENAME, CHARACTER_ENCODING


def load() -> List[Character]:
    chars = []
    with open(CHARS_FILENAME, "r", encoding=CHARACTER_ENCODING) as f:
        json_strs = list(f)
        for json_str in json_strs:
            char = Character.from_json_str(json_str=json_str)
            if char is not None:
                chars.append(char)
    print(f"loaded {len(chars)} chars")
    return chars
