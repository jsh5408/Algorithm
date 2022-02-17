N, M, V = map(int, input().split())

graph = {i:[] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph.keys():
    graph[g].sort()

b = []
d = []

### DFS
visited = {i:0 for i in range(1, N+1)}
def dfs(graph, v):
    print(v, end=' ')
    visited[v] = 1

    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i)
    
dfs(graph, V)
print()

### BFS
visited = {i:0 for i in range(1, N+1)}
queue = [V]
while queue:
    q = queue.pop(0)
    visited[q] = 1
    print(q, end= ' ')
    for i in graph[q]:
        if visited[i] == 0:
            visited[i] = 1
            queue.append(i)