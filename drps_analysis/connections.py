import json
import re

COURSE_ID_REGEX = "[a-z]{4}[0-9]{5}"

DATA = "./data/"
RESULTS = "./results/"

with open(DATA + "courses.json", "r", encoding="utf-8") as f:
    courses = json.loads(f.read())

course_keys = list(courses.keys())

connections = {}

for key in course_keys:
    requirements = courses[key]["entry"]["pre_req"].lower()
    connections[key] = [req for req in re.findall(COURSE_ID_REGEX, requirements) if req in course_keys]

with open(RESULTS + "connections.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(connections))