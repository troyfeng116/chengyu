from src.chengyu.fetch_and_store import fetch_and_store_all
from src.chengyu.load import load


def main() -> int:
    # fetch_and_store_all()
    all_chengyu = load()
    for i in range(min(10, len(all_chengyu))):
        print(all_chengyu[i])
    return 0


if __name__ == "__main__":
    exit(main())
