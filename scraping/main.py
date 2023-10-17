import requests
import bs4

from bs4 import BeautifulSoup
from typing import Union


# URL = "http://www.zd9999.com/cy/index.htm"
URL = "http://www.zd9999.com/cy/htm0/1.htm"
# URL = "http://www.zd9999.com/cy/htm0/4.htm"

START_PATH = "/cy/htm0/1.htm"
BASE_URL = "http://www.zd9999.com"


def scrape(path: str) -> Union[str, None]:
    res = requests.get(f"{BASE_URL}/{path}")
    if res.status_code != 200:
        print(f"error: {res.status_code} reason={res.reason}")
        return None

    html = res.content.decode("gb2312", "ignore")
    soup = BeautifulSoup(html, "html.parser")
    table: bs4.element.Tag = soup.find_all("table")[-3]
    first_row: bs4.element.Tag = table.findChildren("tr")[0]
    cheng_yu = first_row.findChild("td").findChild("font").findChild("b").getText()
    print(f"{path} -> {cheng_yu}")

    try:
        last_row: bs4.element.Tag = table.findChildren("tr")[-1]
        last_cell: bs4.element.Tag = last_row.findChildren("td")[-1]
        next_link_el: bs4.element.Tag = last_cell.findChild("a")
        next_link_href = next_link_el.get("href")
        return next_link_href
    except:
        return None


def main() -> int:
    path = START_PATH
    num_scraped = 0
    while path is not None and num_scraped < 89:
        path = scrape(path=path)
        num_scraped += 1

    return 0


if __name__ == "__main__":
    exit(main())