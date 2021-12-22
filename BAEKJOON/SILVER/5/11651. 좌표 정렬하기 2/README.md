## 좌표 정렬하기 2 - python3
https://www.acmicpc.net/problem/11651

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())
coords = []

for _ in range(N):
    x, y = map(int, stdin.readline().split())
    coords.append((x, y))

coords.sort(key = lambda x: (x[1], x[0]))

for x, y in coords:
    print(x, y)
```
입력받은 좌표들을 y 좌표 -> x 좌표 순으로 기준을 잡고 정렬

![](https://images.velog.io/images/jsh5408/post/1538b11f-98de-45e3-bb93-1a1b1f9eed25/image.png)