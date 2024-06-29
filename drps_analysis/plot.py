from pyvis.network import Network
import networkx as nx
import json

DATA = "./data/"
RESULTS = "./results/"

G = nx.DiGraph()

net = Network(width=1000, height=1000, notebook=True)

with open(RESULTS + "connections.json", "r", encoding="utf-8") as f:
    data = json.loads(f.read())

with open(DATA + "courses.json", "r", encoding="utf-8") as f:
    course_data = json.loads(f.read())

for course in data.keys():
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

net.show("plot.html")