## 11279. 최대 힙 - python3
https://www.acmicpc.net/problem/11279

#### 내 풀이 - 성공
```
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
```
heapq 가 기본적으로 최소 힙으로 되어있으므로
최대 힙을 이용하기 위해서는 두개의 인자를 사용해서 저장해야한다.

(-x, x) 로 저장하면 -x 를 기준으로 오름차순으로 정렬하기 때문에
x 는 결과적으로 내림차순으로 저장되는 효과를 갖게 됨

pop 할 때는 h[1] 을 출력하도록 함

![](https://images.velog.io/images/jsh5408/post/75032c2b-eb26-48fb-b4a6-b7baf54d9cae/image.png)