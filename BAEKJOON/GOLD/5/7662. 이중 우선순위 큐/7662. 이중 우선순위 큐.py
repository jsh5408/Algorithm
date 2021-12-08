from sys import stdin
import heapq

T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    minQ = []
    maxQ = []
    visited = [False] * 1000001
    for i in range(k):
        op, n = map(str, stdin.readline().split())
        if op == "I":
            heapq.heappush(minQ, (int(n), i))
            heapq.heappush(maxQ, (-int(n), i))
            visited[i] = True
        else:
            if n == "-1":
                # maxQ 에서 이미 삭제된 값은 버리기
                while minQ and not visited[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    visited[minQ[0][1]] = False
                    heapq.heappop(minQ)
            elif n == "1":
                # minQ 에서 이미 삭제된 값은 버리기
                while maxQ and not visited[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    visited[maxQ[0][1]] = False
                    heapq.heappop(maxQ)
    while minQ and not visited[minQ[0][1]]: heapq.heappop(minQ)
    while maxQ and not visited[maxQ[0][1]]: heapq.heappop(maxQ)
    print(f'{-maxQ[0][0]} {minQ[0][0]}' if maxQ and minQ else'EMPTY')