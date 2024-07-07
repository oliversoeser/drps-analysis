import json
import re

# RegEx
COURSE_ID_REGEX = "[a-z]{4}[0-9]{5}"

# Paths
RESULTS = "./results/"
DATA = "./results/data/"

# Read courses
with open(f"{DATA}courses.json", "r", encoding="utf-8") as f:
    courses = json.loads(f.read())

course_keys = list(courses.keys())

# Create blank graph
graph = {"nodes": [], "edges": []}

# Add nodes
graph["nodes"] = [{"key": key, "attributes": {"data": courses[key]}} for key in course_keys]

# Add edges
for key in course_keys:
    pre_req = courses[key]["entry"]["pre_req"].lower()
    for req in re.findall(COURSE_ID_REGEX, pre_req):
        if req in course_keys:
            graph["edges"].append({"source": req, "target": key, "undirected": False})

# Save graph
with open(f"{RESULTS}graph.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(graph))