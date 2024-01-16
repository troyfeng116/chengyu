import requests

from bs4 import BeautifulSoup, element
from typing import List, Union

from src.models.character import Character

BASE_CHARACTERS_URL = "http://hanzidb.org"
BASE_CHARACTERS_PATH = "/character-list"


def format_path(page_number: int) -> str:
    return (
        f"{BASE_CHARACTERS_PATH}?page={page_number}"
        if page_number > 1
        else BASE_CHARACTERS_PATH
    )


def extract_character(row: element.Tag) -> Union[Character, None]:
    try:
        cols = row.findChildren("td")
        char = cols[0].get_text()
        pinyin = cols[1].get_text()
        definition = cols[2].get_text()
        stroke_count = int(cols[4].get_text())
        return Character(
            char=char, pinyin=pinyin, definition=definition, stroke_count=stroke_count
        )
    except Exception as e:
        # print(e)
        return None


def scrape_characters_from_page(path: str) -> List[Character]:
    res = requests.get(f"{BASE_CHARACTERS_URL}{path}")
    if res.status_code != 200:
        print(
            f"error ({BASE_CHARACTERS_URL}{path}): {res.status_code} reason={res.reason}"
        )
        return []

    html = res.content.decode("utf-8", "ignore")
    soup = BeautifulSoup(html, "html.parser")

    table: element.Tag = soup.find_all("table")[0]
    rows: List[element.Tag] = table.findChildren("tr")
    chars: List[Character] = []
    for row in rows[1:]:
        char = extract_character(row=row)
        chars.append(char)

    return chars


def scrape_all_characters() -> List[Character]:
    all_chars = []
    for page_number in range(1, 9):
        chars = scrape_characters_from_page(path=format_path(page_number=page_number))
        all_chars += chars
    return all_chars
