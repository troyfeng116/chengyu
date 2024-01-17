from src.chengyu.scraper import scrape_all_chengyu


def main() -> int:
    all_chengyu = scrape_all_chengyu()
    for c in all_chengyu:
        print(c)

    return 0


if __name__ == "__main__":
    exit(main())
