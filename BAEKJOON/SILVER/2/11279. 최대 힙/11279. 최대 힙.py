from sys import stdin
import heapq

N = int(stdin.readline())
maxheap = []

for _ in range(N):
    x = int(stdin.readline())
    
    if x == 0:
        if maxheap:
            h = heapq.heappop(maxheap)
            print(h[1])
        else:
            print(0)
    else:
        heapq.heappush(maxheap, (-x, x))