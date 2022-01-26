## 1927. 최소 힙 - python3
https://www.acmicpc.net/problem/1927

#### 내 풀이 - 성공
```
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
```
min-heap 을 이용해서 문제 고대로 풀었다

n 이 0 일 때만 heap 에 값이 있는지 판단해서 pop & print / 없으면 print(0)
자연수면 heappush

![](https://images.velog.io/images/jsh5408/post/609985fd-f5b5-43e3-9bb5-23dccc64b6db/image.png)