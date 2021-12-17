## 11286. 절댓값 힙 - python3
https://www.acmicpc.net/problem/11286

#### 내 풀이 - 성공
```
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
```
최대힙을 저장하듯이 (절댓값, 값) 으로 묶어서 저장
=> 절댓값을 기준으로 정렬

출력할 때는 원래 값을 출력 => h[1]

![](https://images.velog.io/images/jsh5408/post/4ba6fb91-9668-4e6c-a3b6-c796a3d69418/image.png)