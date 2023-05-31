from heapq import *

def prims(graph, start, parent, distance, visited):
    bag = []
    heappush(bag, [0, start])  #[distance,node]
    distance[start] = 0
    parent[start] = -1
    while bag:
        d, n = heappop(bag)
        if not visited[n]:
            visited[n] = 'v'
            for cd, cn in graph[n]:
                if distance[cn] > cd and not visited[cn]:
                    parent[cn] = n
                    distance[cn] = cd
                    heappush(bag, [cd, cn])

    print(parent)
    print(distance)
  

size = int(input("Enter size of graph: "))
# edges = int(input("Enter number of edges: "))

# G = [[0]*size for _ in range(size)]
# inp = []

# for i in range(edges):
#     edge = []
#     src, dest, wei = input("Enter src, dest, weight: ").split()
#     src = int(src)
#     dest = int(dest)
#     wei = int(wei)
#     G[src][dest] = wei
#     edge.append(src)
#     edge.append(dest)
#     edge.append(wei)
#     inp.append(edge)




ipt = [[1,2,1], [2, 3, 4,], [3,4,1], [4,5,2], [1,5,3], [2,5,2], [2,4,1]] #[startnode, endnode, dist]
n = 5

graph = {}
parent = {}
distance = {}
visited = {}

for i in range(1, 1+n):
    graph[i] = []
    parent[i] = None
    distance[i] = 10**8+1
    visited[i] = 0

for u, v, d in ipt:
    graph[u].append([d, v])
    graph[v].append([d, u])

#print(graph)


start = 5

prims(graph, start, parent, distance, visited)

for k, v in parent.items():
    if v != -1:
        print(f'{v} - {k}')

tot = 0
for k, v  in distance.items():
    tot+=v

print()
print(tot)