from src.scraping.characters.scrape_characters import (
    scrape_all_characters,
)


def main() -> int:
    all_chars = scrape_all_characters()
    for c in all_chars:
        print(c)
    print(len(all_chars))
    return 0


if __name__ == "__main__":
    exit(main())
