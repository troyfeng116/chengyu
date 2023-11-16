from src.scraping.scrape import scrape, START_PATH


def main() -> int:
    path = START_PATH
    num_scraped = 0
    while path is not None and num_scraped < 89:
        path = scrape(path=path)
        num_scraped += 1

    return 0


if __name__ == "__main__":
    exit(main())
