from heapq import *

def dijkstra(graph, start, visited, distance):
    distance[start] = 0
    bag = []
    heappush(bag, [0, start])

    while bag:
        d, n = heappop(bag)
        visited[n] = 'v'
        for cd, cn in graph[n]:
            if distance[n] + cd < distance[cn] and not visited[cn]:
                distance[cn] = distance[n] + cd
                heappush(bag,[distance[n] + cd, cn])
    print(distance)


N = int(input("Enter Size of Graph: "))
# edges = int(input("Enter number of edges: "))
# inp = []

# G = [[0]*N for _ in range(N)]

# for i in range(edges):
#     edge = []
#     src, dest, weight = input("Enter src, dest, weight: ").split()
#     edge.append(int(src))
#     edge.append(int(dest))
#     edge.append(int(weight))
#     inp.append(edge)
#     G[int(src)][int(dest)] = int(weight

ipt = [[1,3,2], [1,2,1], [2,3,1], [2,5,1], [3,4,2], [2,5,2], [5,4,5]] #[startnode, endnode, dist]
n = 5

graph = {}
distance = {}
visited = {}

for i in range(1, 1+n):
    graph[i] = []
    distance[i] = 10**8+1
    visited[i] = 0

for u, v, d in ipt:
    graph[u].append([d, v])
    graph[v].append([d, u])

#print(graph)


start = 1

dijkstra(graph, start, visited, distance)
