import requests
import time
import re
import os
import json
from extractor import extract

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

index = get("cx_subindex.htm")

schools = re.findall("cx_sb_[a-z]{4}.htm", index)

for school in schools:
    catalogue = get(school)

    courses = re.findall("cx[a-z]{4}[0-9]{5}\.htm", catalogue)

    for course in courses:
        try:
            page = extract(get(course))
            f = open("./scraped/" + course.replace("htm", "json"), "w", encoding="utf-8")
            f.write(json.dumps(page))
            f.close()
        except:
            print(f"Course {course} was not read, the URL likely does not exist.")
