import requests


def get_url(url: str) -> requests.Response:
    res = requests.get(url)
    if res.status_code != 200:
        print(f"[fetch] error {res.status_code} on GET {url}: {res.reason}")
        return None
    return res
