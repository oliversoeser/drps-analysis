from extractor import extract
from fetcher import get
import json
import re

DATA = "./data/"

index = get("cx_subindex.htm")
schools = re.findall("cx_sb_[a-z]{4}.htm", index)

for school in schools:
    catalogue = get(school)

    courses = re.findall("cx[a-z]{4}[0-9]{5}\.htm", catalogue)

    for course in courses:
        try:
            page = extract(get(course))
            f = open(DATA + course.replace("htm", "json"), "w", encoding="utf-8")
            f.write(json.dumps(page))
            f.close()
        except:
            print(f"Course {course} was not read, the URL likely does not exist.")
