from pyvis.network import Network
import networkx as nx
import json

G = nx.DiGraph()

with open("connections.json", "r", encoding="utf-8") as f:
    data = json.loads(f.read())

for course in data.keys():
    if course.startswith("math"):
        G.add_node(course)
        for prereq in data[course]:
            if not prereq.startswith("math"):
                G.add_node(course)
            G.add_edge(course, prereq)

net = Network(width=2000, height=1000, notebook=True)
net.from_nx(G)

net.show("plot.html")