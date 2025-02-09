import heapq

class GraphCycleError(Exception):
    def __init__(self):
        super().__init__("DAG was expected, but the graph has a cycle.")

WHITE = 0
GREY = 1
BLACK = 2

# Standard graph using adjacency lists
class Graph:
    def __init__(self):
        self.adj = []
        self.n = 0

        self.state = None
        self.L = None

        self.visited = None
        self.CC = None

    def addVertex(self):
        self.adj.append([])
        self.n += 1
        return self.n - 1

    def addEdge(self, start, end):
        self.adj[start].append(end)

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
    
    def connComp(self):
        self.visited = [False] * self.n
        self.CC = []

        for v in range(self.n):
            if self.visited[v] == False:
                self.CC.append([])
                self.ccFromVertex(v)

        return self.CC

    def ccFromVertex(self, v):
        self.visited[v] = True
        self.CC[len(self.CC)-1].append(v)

        for w in self.adj[v]:
            if self.visited[w] == False:
                self.ccFromVertex(w)

class PriorityVertex:
    def __init__(self, id, priority):
        self.id = id
        self.priority = priority
    
    # Comparison operations are swapped to turn the heapq min-heap into a max-heap
    def __lt__(self, other):
        return self.priority > other.priority

    def __gt__(self, other):
        return self.priority < other.priority

# Graph where each vertex has an associated priority
class PriorityGraph(Graph):
    def __init__(self):
        super().__init__()

        self.V = []
        self.priorities = []

        self.V_heap = None
        self.adj_heaps = None

    def addVertex(self, priority):
        self.priorities.append(priority)
        self.V.append(PriorityVertex(len(self.V), priority))
        return super().addVertex()
    
    def addEdge(self, start, end):
        self.adj[start].append(PriorityVertex(end, self.priorities[end]))
    
    def topSort(self):
        self.V_heap = self.V.copy()
        heapq.heapify(self.V_heap)

        self.adj_heaps = []
        for v in range(self.n):
            self.adj_heaps.append(self.adj[v].copy())
            heapq.heapify(self.adj_heaps[v])

        self.state = [WHITE] * self.n
        self.L = []

        while len(self.V_heap) != 0:
            v = heapq.heappop(self.V_heap).id
            if self.state[v] == WHITE:
                self.sortFromVertex(v)
        
        return self.L
    
    def sortFromVertex(self, v):
        self.state[v] = GREY

        while len(self.adj_heaps[v]) != 0:
            w = heapq.heappop(self.adj_heaps[v]).id
            if self.state[w] == WHITE:
                self.sortFromVertex(w)
            elif self.state[w] == GREY:
                raise GraphCycleError
        
        self.state[v] = BLACK
        self.L.append(v)