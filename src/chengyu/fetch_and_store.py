import os

from src.chengyu.scraper import scrape_all_chengyu, CHENGYU_ENCODING
from src.chengyu.model import ChengYu


dir_path = os.path.dirname(os.path.realpath(__file__))
CHENGYU_FILENAME = f"{dir_path}/chengyu.jsonl"


def fetch_and_store_all():
    all_chengyu = scrape_all_chengyu()
    print(f"fetched {len(all_chengyu)} chengyu")
    all_chengyu_strs = map(lambda ch: ch.to_json_str(), all_chengyu)
    all_chengyu_strs = [
        chengyu_str for chengyu_str in all_chengyu_strs if chengyu_str is not None
    ]
    with open(CHENGYU_FILENAME, "w", encoding=CHENGYU_ENCODING) as f:
        for chengyu_str in all_chengyu_strs:
            f.write(chengyu_str + "\n")
