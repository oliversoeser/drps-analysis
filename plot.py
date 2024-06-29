from pyvis.network import Network
import networkx as nx
import json

G = nx.DiGraph()

net = Network(width=1000, height=1000, notebook=True)

def id_to_color(id: str) -> str:
    cat = id[:4]
    if cat == "math":
        return "#d63d2f"
    elif cat == "infr":
        return "#969e9d"
    elif cat == "phys":
        return "#7df2e4"
    elif cat == "bust":
        return "#99743d"
    elif cat == "ecnm":
        return "#e8971e"
    elif cat == "bilg":
        return "#3eef5e"
    elif cat == "psyl":
        return "#643eef"
    return "#9819e8"

with open("connections.json", "r", encoding="utf-8") as f:
    data = json.loads(f.read())

with open("courses.json", "r", encoding="utf-8") as f:
    course_data = json.loads(f.read())

subjects = []

for course in data.keys():
    subjects.append(course[:4])
    if course[:4] in ["math", "infr", "phys", "ecnm", "bust", "bilg", "psyl"]:
        G.add_node(course)
        for prereq in data[course]:
            G.add_edge(course, prereq)

singletons = []
for node in G.nodes:
    if G.degree[node] == 0:
        singletons.append(node)

G.remove_nodes_from(singletons)

net.from_nx(G)

for node in net.nodes:
    course_id = node["label"]
    title = str(course_data[course_id]["title"])
    title = title.replace("Undergraduate Course: ", "")
    title = title.replace("Postgraduate Course: ", "")
    title = title.replace("&amp;", "&")
    title = title[:title.rfind("(")]
    node["title"] = course_id
    node["label"] = title
    node["color"] = id_to_color(course_id)

    #if id_to_color(course_id) == "#9819e8":
    #    print(course_id)

print(sorted(list(set(subjects))))

net.show("plot.html")