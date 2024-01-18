from src.characters.fetch_and_store import fetch_and_store_all
from src.characters.load import load


def main() -> int:
    # fetch_and_store_all()
    all_chars = load()
    for i in range(min(10, len(all_chars))):
        print(all_chars[i])
    return 0


if __name__ == "__main__":
    exit(main())
