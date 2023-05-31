def dfs(graph, node, visited = set()):
    print(node)
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph, child, visited)


ipt = [[1,2], [1,5], [2, 3], [2,4], [2, 5], [3, 4], [3, 6], [4, 5], [4, 6], [5, 6]]
graph = {}
n = 6

for i in range(1, n+1):
    graph[i] = []

for (u, v) in ipt:
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1)

'''class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for _ in range(v)]
    
    def addEdge(self, src, dest):
        self.adj[src].append(dest)

    def DFS(self, start, visited):
        visited[start] = 1
        print(start, end = " ")
        
        for a in self.adj[start]:
            if visited[a] == 0:
                self.DFS(a, visited)

size = int(input("Enter size of Graph: "))
edges = int(input("Enter number of edges: "))

graph = Graph(size)

for i in range(edges):
    src, dest = input("Enter edge between (src dest): ").split()
    src = int(src)
    dest = int(dest)
    graph.addEdge(src, dest)

start = int(input("Enter starting edge: "))
visited = [0]*(size)
graph.DFS(start, visited)'''