## 9184. 신나는 함수 실행 - python3
https://www.acmicpc.net/problem/9184

#### 내 풀이 - 성공
```
from sys import stdin
import collections

dp = collections.defaultdict(int)

def w(a, b, c):
    global dp

    if (a, b, c) in dp:
        return dp[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        dp[(a, b, c)] = 1
    elif a > 20 or b > 20 or c > 20:
        dp[(a, b, c)] = w(20, 20, 20)
    elif a < b and b < c:
        dp[(a, b, c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[(a, b, c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[(a, b, c)]

while True:
    a, b, c = map(int, stdin.readline().split())

    if a == -1 and b == -1 and c == -1:
        break
    
    print(f'w({a}, {b}, {c}) = ', end='')
    print(w(a, b, c))
```
while True 문을 돌려서 입력을 받고 a, b, c 모두 -1 일 때 break 하도록 함

재귀는 현재 조합의 값이 이미 구한 값이면 그 값을 사용하고
아니면 조건대로 재귀 돌려서 dp 값 구한 후,
최종적으로 dp 값 return

![](https://images.velog.io/images/jsh5408/post/b0d4fbd4-5430-465c-ba3a-5f2e77b6990d/image.png)