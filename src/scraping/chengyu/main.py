from scrape_chengyu import scrape_chengyu, START_PATH


def main() -> int:
    path = START_PATH
    num_scraped = 0
    while path is not None and num_scraped < 89:
        path = scrape_chengyu(path=path)
        num_scraped += 1

    return 0


if __name__ == "__main__":
    exit(main())
