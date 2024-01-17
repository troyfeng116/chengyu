import os

from src.characters.scraper import (
    scrape_all_characters,
    CHARACTER_ENCODING,
)


dir_path = os.path.dirname(os.path.realpath(__file__))
CHARS_FILENAME = f"{dir_path}/chars.jsonl"


def fetch_and_store_all():
    all_chars = scrape_all_characters()
    print(f"fetched {len(all_chars)} chars")
    all_char_strs = map(lambda ch: ch.to_json_str(), all_chars)
    all_char_strs = [ch_str for ch_str in all_char_strs if ch_str is not None]
    with open(CHARS_FILENAME, "w", encoding=CHARACTER_ENCODING) as f:
        for char_str in all_char_strs:
            f.write(char_str + "\n")
