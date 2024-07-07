from helper.extract import extract
from helper.fetch import get
import json
import re

# RegEx
SCHOOL_REGEX = "cx_sb_[a-z]{4}\\.htm"
COURSE_REGEX = "cx[a-z]{4}[0-9]{5}\\.htm"
COURSE_ID_REGEX = "[a-z]{4}[0-9]{5}"

# Paths
RESULTS = "./results/"
DATA = "./results/data/"

courses_data = {}

# Index all the school's pages
schools = re.findall(SCHOOL_REGEX, get("cx_subindex.htm"))

for school in schools:
    # Find all the course pages
    courses = re.findall(COURSE_REGEX, get(school))

    for course in courses:
        # Get ID
        course_id = re.search(COURSE_ID_REGEX, course).group()

        # Extract and save the data
        page = extract(get(course))
        courses_data[course_id] = page

        with open(f"{DATA}{course_id}.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(page))

with open(f"{DATA}courses.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(courses_data))