from sys import stdin
import collections

N = int(stdin.readline())
C = int(stdin.readline())
network = {i:[] for i in range(1, N+1)}

for i in range(C):
    a, b = map(int, stdin.readline().split())
    network[a].append(b)
    network[b].append(a)

computers = [1]*(N+1)
computers[0] = 0

queue = collections.deque([1])

while queue:
    q = queue.popleft()
    computers[q] = 0
    for n in network[q]:
        if computers[n]:
            queue.append(n)

print(computers.count(0)-2)