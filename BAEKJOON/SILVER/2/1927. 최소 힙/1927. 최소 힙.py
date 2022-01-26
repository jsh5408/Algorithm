import heapq
from sys import stdin

N = int(stdin.readline())
heap = []
for i in range(N):
    n = int(stdin.readline())
    if n == 0:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, n)