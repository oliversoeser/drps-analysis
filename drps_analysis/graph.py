import json
import re
import random

COURSE_ID_REGEX = "[a-z]{4}[0-9]{5}"

RESULTS = "./results/"
DATA = "./results/data/"

with open(DATA + "courses.json", "r", encoding="utf-8") as f:
    courses = json.loads(f.read())

course_keys = list(courses.keys())

graph = {"nodes": [], "edges": []}

graph["nodes"] = [{"key": key, "attributes": {"data": courses[key]}} for key in course_keys]

for key in course_keys:
    pre_req = courses[key]["entry"]["pre_req"].lower()
    for req in re.findall(COURSE_ID_REGEX, pre_req):
        if req in course_keys:
            graph["edges"].append({"source": req, "target": key, "undirected": False})

with open(RESULTS + "graph.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(graph))