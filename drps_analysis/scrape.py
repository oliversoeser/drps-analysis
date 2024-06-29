from helper.extract import extract
from helper.fetch import get
import json
import re

DATA = "./data/"

SCHOOL_REGEX = "cx_sb_[a-z]{4}\\.htm"
COURSE_REGEX = "cx[a-z]{4}[0-9]{5}\\.htm"

schools = re.findall(SCHOOL_REGEX, get("cx_subindex.htm"))

courses_data = {}

with open("./log.txt", "w", encoding="utf-8") as f:
    f.write("")

for school in schools:
    courses = re.findall(COURSE_REGEX, get(school))

    for course in courses:
        try:
            page = extract(get(course))
            courses_data[course[2:11]] = page
            with open(DATA + course.replace("htm", "json"), "w", encoding="utf-8") as f:
                f.write(json.dumps(page))
        except Exception as e:
            with open("./log.txt", "a", encoding="utf-8") as f:
                f.write(f"Failed to extract data from {course}, it likely does not exist: " + str(e))

with open(DATA + "courses.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(courses_data))