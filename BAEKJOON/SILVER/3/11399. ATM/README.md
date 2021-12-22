## 11399. ATM - python3
https://www.acmicpc.net/problem/11399

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))

P.sort()

ans = 0

for i in range(N):
    ans += P[i] * (N-i)

print(ans)
```
`N = 5` 이고 `[P1, P2, P3, P4, P5]` 의 순서일 때
시간의 합은 `P1 * 5 + P2 * 4 + P3 * 3 + P4 * 2 + P5 * 1` 이 된다.

여기서 최소 시간합이 되려면 상대적으로 큰 숫자를 곱하는 앞 순서의 P 값들이 작아야 한다.

따라서 정렬 후 `P * N-i` 를 모두 더해주면 된다.

![](https://images.velog.io/images/jsh5408/post/11dacd86-ff11-4988-bd92-c0692d4c6a35/image.png)