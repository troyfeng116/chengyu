from typing import List

from src.chengyu.model import ChengYu
from src.chengyu.fetch_and_store import CHENGYU_FILENAME, CHENGYU_ENCODING


def load() -> List[ChengYu]:
    all_chengyu = []
    with open(CHENGYU_FILENAME, "r", encoding=CHENGYU_ENCODING) as f:
        json_strs = list(f)
        for json_str in json_strs:
            char = ChengYu.from_json_str(json_str=json_str)
            if char is not None:
                all_chengyu.append(char)

    print(f"loaded {len(all_chengyu)} chengyu")
    return all_chengyu
