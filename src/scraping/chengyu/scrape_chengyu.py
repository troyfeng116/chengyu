from bs4 import BeautifulSoup, element
from typing import List, Tuple, Union

from src.models.chengyu import ChengYu
from src.scraping.fetch import get_url

# URL = "http://www.zd9999.com/cy/index.htm"
# URL = "http://www.zd9999.com/cy/htm0/1.htm"
# URL = "http://www.zd9999.com/cy/htm0/4.htm"


START_PATH = "/cy/htm0/1.htm"
BASE_URL = "http://www.zd9999.com"


def scrape_chengyu_from_page(
    path: str,
) -> Tuple[Union[ChengYu, None], Union[str, None]]:
    res = get_url(f"{BASE_URL}{path}")
    if res is None:
        return None, None

    html = res.content.decode("gbk", "ignore")
    soup = BeautifulSoup(html, "html.parser")

    table: element.Tag = soup.find_all("table")[-3]
    rows: List[element.Tag] = table.findChildren("tr")

    first_row: element.Tag = rows[0]
    chengyu_chars = first_row.get_text().strip()

    second_row: element.Tag = rows[1]
    nested_rows: List[element.Tag] = second_row.findChild("td").findChildren("tr")
    pinyin = nested_rows[0].findChildren("td")[1].getText().strip()
    fanyi = nested_rows[1].findChildren("td")[1].getText().strip()
    source = nested_rows[2].findChildren("td")[1].getText().strip()
    example = nested_rows[3].findChildren("td")[1].getText().strip()

    # print(f"{path} -> {chengyu_chars}: {pinyin} -> {fanyi}")
    chengyu = ChengYu(
        chars=chengyu_chars,
        pinyin=pinyin,
        definition=fanyi,
        source=source,
        example=example,
    )

    try:
        last_row: element.Tag = rows[-1]
        last_cell: element.Tag = last_row.findChildren("td")[-1]
        next_link_el: element.Tag = last_cell.findChild("a")
        next_link_href = next_link_el.get("href")
        return chengyu, next_link_href
    except:
        return None, None


def scrape_all_chengyu() -> List[ChengYu]:
    path = START_PATH
    all_chengyu = []
    while path is not None and len(all_chengyu) < 9:
        chengyu, path = scrape_chengyu_from_page(path=path)
        if chengyu is not None:
            all_chengyu.append(chengyu)

    return all_chengyu
