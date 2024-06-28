from extractor import extract
from fetcher import get
import json
import re

DATA = "./data/"

SCHOOL_REGEX = "cx_sb_[a-z]{4}.htm"
COURSE_REGEX = "cx[a-z]{4}[0-9]{5}\.htm"

schools = re.findall(SCHOOL_REGEX, get("cx_subindex.htm"))

for school in schools:
    courses = re.findall(COURSE_REGEX, get(school))

    for course in courses:
        try:
            page = extract(get(course))
            with open(DATA + course.replace("htm", "json"), "w", encoding="utf-8") as f:
                f.write(json.dumps(page))
        except:
            print(f"Failed to extract data from {course}, it likely does not exist.")