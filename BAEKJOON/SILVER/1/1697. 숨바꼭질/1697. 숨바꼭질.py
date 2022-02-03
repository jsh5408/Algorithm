import sys
import collections

N, K = map(int, sys.stdin.readline().split())

queue = collections.deque()
dist = collections.defaultdict(int)
visited = collections.defaultdict(int)

queue.append(N)
visited[N] = 1

# bfs
while queue:
    node = queue.popleft()
    if node == K:
        print(dist[node])
        break
    for next_node in (node-1, node+1, 2*node):
        if visited[next_node] != 1 and next_node <= 100000:
            queue.append(next_node)
            visited[next_node] = 1
            dist[next_node] = dist[node] + 1