import requests
import time
import os

BASE_URL = "http://www.drps.ed.ac.uk/24-25/dpt/"
CACHE = "./cache/"

def get(url: str, wait: int = 2) -> str:
    if os.path.isfile(CACHE + url):
        with open(CACHE + url, "r", encoding="utf-8") as f:
            text = f.read()
        return text
    else:
        res = requests.get(BASE_URL + url)
        with open(CACHE + url, "w", encoding="utf-8") as f:
            f.write(res.text)
        time.sleep(wait)
        return res.text