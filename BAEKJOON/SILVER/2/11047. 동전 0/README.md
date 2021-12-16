## 11047. 동전 0 - python3
https://www.acmicpc.net/problem/11047

#### 내 풀이 - 성공
```
from sys import stdin

N, K = map(int, stdin.readline().split())
coins = []
ans = 0

for _ in range(N):
    c = int(stdin.readline())
    coins.append(c)

for i in range(N-1, -1, -1):
    if coins[i] <= K:
        ans += K // coins[i]
        K = K % coins[i]

print(ans)
```
coins 는 이미 정렬된 상태이므로 큰 값부터 K 에서 빼기 위해 역순으로 for 문 돌리기

coins[i] 가 K 보다 작아지는 순간의 coins[i] 를 K 에서 최대한 많이 빼기
=> K // coins[i]
(반복문으로 직접 빼면 시간 초과)

![](https://images.velog.io/images/jsh5408/post/4b424390-44b1-43ef-a79b-b8e14017b026/image.png)