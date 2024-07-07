import requests
import time
import os

BASE_URL = "http://www.drps.ed.ac.uk/24-25/dpt/"
CACHE = "./cache/"

def get(url: str, wait: int = 2) -> str:
    path = CACHE + url

    # Check if the file has been cached
    if os.path.isfile(path):
        # Read from the cache
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        return text
    else:
        # Download and save to the cache
        res = requests.get(BASE_URL + url)
        with open(path, "w", encoding="utf-8") as f:
            f.write(res.text)
        
        # Wait to ensure the server won't be overwhelmed
        time.sleep(wait)

        return res.text