import json
import re

COURSE_ID_REGEX = "[a-z]{4}[0-9]{5}"

with open("courses.json", "r", encoding="utf-8") as f:
    courses = json.loads(f.read())

course_keys = list(courses.keys())

connections = {}

for key in course_keys:
    requirements = courses[key]["entry"]["pre_req"].lower()
    connections[key] = re.findall(COURSE_ID_REGEX, requirements)

with open("connections.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(connections))