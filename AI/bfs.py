def bfs(graph, visited):
    queue = []
    answer = []
    queue.append(1)
    visited[1] = True
    while queue:
        temp = queue.pop(0)
        print(temp)
        for child in graph[temp]:
            if not visited[child]:
                queue.append(child)
                visited[child] = True





ipt = [[1,2],[2, 3], [1,6], [3,6], [3, 4], [3, 6], [4, 5], [4, 6], [5, 6]]
graph = {}
visited = {}
n = 9

for i in range(1, n+1):
    graph[i] = []
    visited[i] = False

for (u, v) in ipt:
    graph[u].append(v)
    graph[v].append(u)

bfs(graph, visited)

'''from collections import deque
 
class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(v)]

    def addEdge(self, src, dest):
        self.adj[src].append(dest)

    def recursiveBFS(self, q, discovered):
        if not q:
            return
        # dequeue front node and print it
        v = q.popleft()
        print(v, end=' ')
        # do for every edge (v, u)
        for u in graph.adj[v]:
            if not discovered[u]:
                # mark it as discovered and enqueue it
                discovered[u] = True
                q.append(u)
        self.recursiveBFS(graph, q, discovered)


size = int(input("Enter size of Graph: "))
edges = int(input("Enter number of edges: "))

graph = Graph(size)

for i in range(edges):
    src, dest = input("Enter edge between (src dest): ").split()
    src = int(src)
    dest = int(dest)
    graph.addEdge(src, dest)


visited = [0]*(size)
q = deque()

start = int(input("Enter starting edge: "))

visited[start] = True
q.append(start)

graph.recursiveBFS(q, visited)'''