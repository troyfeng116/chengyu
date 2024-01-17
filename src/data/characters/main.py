from src.data.characters.fetch_and_store import fetch_and_store_all
from src.data.characters.load import load


def main() -> int:
    # fetch_and_store_all()
    chars = load()
    print(len(chars))
    for i in range(10):
        print(chars[i])
    return 0


if __name__ == "__main__":
    exit(main())
