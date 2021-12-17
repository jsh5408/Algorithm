## 11650. 좌표 정렬하기 - python3
https://www.acmicpc.net/problem/11650

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())
coords = []

for _ in range(N):
    x, y = map(int, stdin.readline().split())
    coords.append((x, y))

coords.sort(key = lambda x: (x[0], x[1]))

for x, y in coords:
    print(x, y)
```
입력받은 좌표들을 sort() 의 lambda 식을 이용

x 좌표 -> y 좌표 의 우선순위로 정렬

![](https://images.velog.io/images/jsh5408/post/b2684713-b51c-491f-bc97-3ad5fec1b531/image.png)