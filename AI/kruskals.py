def find(graph, node):
    if graph[node]<0:
        return node
    else:
        temp = find(graph, graph[node])
        graph[node] = temp
        return temp
    

def union(graph, a, b, answer):
    ta = a
    tb = b
    a = find(graph, a)
    b = find(graph, b)

    if a==b:
        pass
    else:
        answer.append([ta, tb])
        if graph[a] < graph[b]:
            graph[a] = graph[a] + graph[b]
            graph[b] = a
        
        else:
            graph[b] = graph[a] + graph[b]
            graph[a] = b



ipt = [[1,2,3], [1,3,3], [2,6,4], [3,4,1], [4,5,5], [6,5,6], [7,5,7]]

n = 7
answer = []
tot = 0
ipt = sorted(ipt, key=lambda ipt:ipt[2])

graph = [-1] * (n+1)

for u, v, d in ipt:
    union(graph, u, v, answer)

for item in answer:
    print(item)

for item in answer:
    tot += ipt[item[0]][item[1]]
print(tot)

# N = int(input("Enter Size of Graph: "))
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
#     G[int(src)][int(dest)] = int(weight)
#     G[int(dest)][int(src)] = int(weight)
