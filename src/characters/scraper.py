from bs4 import BeautifulSoup, element
from typing import List, Union

from src.characters.model import Character
from src.utils.fetch import get_url

BASE_CHARACTERS_URL = "http://hanzidb.org"
BASE_CHARACTERS_PATH = "/character-list"
CHARACTER_ENCODING = "utf-8"


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
        try:
            stroke_count = int(cols[4].get_text())
        except ValueError:
            stroke_count = 0
        return Character(
            char=char, pinyin=pinyin, definition=definition, stroke_count=stroke_count
        )
    except Exception as e:
        print(
            f"[scrape_characters.extract_character] unable to extract character from soup tag {row}: {e}"
        )
        return None


def scrape_characters_from_page(path: str) -> List[Character]:
    res = get_url(url=f"{BASE_CHARACTERS_URL}{path}")
    if res is None:
        return []

    html = res.content.decode(CHARACTER_ENCODING, "ignore")
    soup = BeautifulSoup(html, "html.parser")

    table: element.Tag = soup.find_all("table")[0]
    rows: List[element.Tag] = table.findChildren("tr")
    chars: List[Character] = []
    for row in rows[1:]:
        char = extract_character(row=row)
        if char is not None:
            chars.append(char)

    return chars


def scrape_all_characters() -> List[Character]:
    all_chars = []
    for page_number in range(1, 819):
        if page_number % 10 == 0:
            print(page_number)
        chars = scrape_characters_from_page(path=format_path(page_number=page_number))
        all_chars.extend(chars)
    return all_chars
