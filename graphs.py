import heapq

class GraphCycleError(Exception):
    def __init__(self):
        super().__init__("DAG was expected, but the graph has a cycle.")

WHITE = 0
GREY = 1
BLACK = 2

# Edge from Vertex a to Vertex b
class Edge:
    a, b = None, None

    def __init__(self, start, end):
        self.a, self.b = start, end

# Graph using adjacency lists
class Graph:
    adj = []
    n = 0

    state = None
    L = None

    def addVertex(self):
        self.adj.append([])
        self.n += 1
        return self.n - 1

    def addEdge(self, start_id, end_id):
        self.adj[start_id].append(end_id)

    def topSort(self):
        self.state = [WHITE] * self.n
        self.L = []

        for v in range(self.n):
            if self.state[v] == WHITE:
                self.sortFromVertex(v)
        
        return self.L
    
    def sortFromVertex(self, v):
        self.state[v] = GREY

        for w in self.adj[v]:
            if self.state[w] == WHITE:
                self.sortFromVertex(w)
            elif self.state[w] == GREY:
                raise GraphCycleError
        
        self.state[v] = BLACK
        self.L.append(v)

class PriorityVertex:
    id, priority = None, None

    def __init__(self, id, priority):
        self.id = id
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority

    def __gt__(self, other):
        return self.priority > other.priority

class PriorityGraph(Graph):
    priorities = []

    def addVertex(self, priority):
        self.priorities.append(priority)
        return super().addVertex()
    
    def topSort(self):
        self.state = [WHITE] * self.n
        self.L = []

        for v in range(self.n):
            if self.state[v] == WHITE:
                self.sortFromVertex(v)
        
        return self.L