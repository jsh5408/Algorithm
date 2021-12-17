from sys import stdin
import heapq

N = int(stdin.readline())
heap = []

for _ in range(N):
    x = int(stdin.readline())
    
    if x == 0:
        if heap:
            h = heapq.heappop(heap)
            print(h[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
