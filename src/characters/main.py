from src.characters.fetch_and_store import fetch_and_store_all
from src.characters.load import load


def main() -> int:
    # fetch_and_store_all()
    chars = load()
    for i in range(10):
        print(chars[i])
    return 0


if __name__ == "__main__":
    exit(main())
