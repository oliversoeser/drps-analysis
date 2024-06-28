import requests
import time
import os

BASE_URL = "http://www.drps.ed.ac.uk/24-25/dpt/"
CACHE = "./cache/"

def get(url: str, wait: int = 2) -> str:
    if os.path.isfile(CACHE + url):
        f = open(CACHE + url, "r", encoding="utf-8")
        text = f.read()
        f.close()
        return text
    else:
        print(url, "not in cache, downloading...")
        res = requests.get(BASE_URL + url)
        f = open(CACHE + url, "w", encoding="utf-8")
        f.write(res.text)
        f.close()
        time.sleep(wait)
        return res.text