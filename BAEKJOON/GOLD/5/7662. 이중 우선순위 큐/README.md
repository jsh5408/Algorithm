## 7662. 이중 우선순위 큐 - python3
https://www.acmicpc.net/problem/7662

#### 내 풀이 - 실패
```
from sys import stdin
import heapq

T = int(stdin.readline())

for _ in range(T):
    k = int(stdin.readline())
    minQ = []
    maxQ = []
    cnt = 0
    for i in range(k):
        op, n = map(str, stdin.readline().split())
        if op == "I":
            cnt += 1
            heapq.heappush(minQ, int(n))
            heapq.heappush(maxQ, (-int(n), int(n)))
        else:
            if cnt == 0:
                continue
            if n == "-1" and cnt > 0:
                heapq.heappop(minQ)
            elif n == "1" and cnt > 0:
                heapq.heappop(maxQ)
            cnt -= 1
            if cnt == 0:
                minQ = []
                maxQ = []
    if cnt > 0:
        print(str(maxQ[0][1]) + " " + str(minQ[0]))
    else:
        print("EMPTY")
```
min-heap 과 max-heap 두가지를 이용

최솟값은 minQ 에서 삭제, 최댓값은 maxQ 에서 삭제하도록 함
cnt 로 실제 큐에 남아있는 원소의 개수를 세줌
모두 삭제된 경우는 minQ, maxQ 초기화

하지만 삭제를 할 때 하나의 큐만 삭제되므로 다른 큐에 남아있는 값이 문제를 일으킴...

#### 다른 사람의 풀이
```
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
```
visited 를 함께 사용하고
minQ, maxQ 저장 시, 인덱스 값을 함께 저장 => (int(n), i)
인덱스는 고유한 값이라는 점을 이용해서 visited 값에 T/F 적용

push 할 때는 visited[i] = True

pop 할 때는 다른 큐에서 삭제된 값을 버리고 pop 하도록 함 => 동기화
(visited[minQ[0][1]] 가 False 인 애들은 다 버리기)

마지막으로 minQ, maxQ 모두 동기화 한 번 더 해주고
format 에 맞게 print 하거나 EMPTY print


![](https://images.velog.io/images/jsh5408/post/a1912db2-af2c-4f91-a08f-9fd30b268119/image.png)