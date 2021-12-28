## 2798. 블랙잭 - python3
https://www.acmicpc.net/problem/2798

#### 내 풀이 - 성공
```
from sys import stdin

N, M = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))

cards.sort()

ans = 0

for a in range(len(cards)-1, 1, -1):
    for b in range(a-1, 0, -1):
        tmp = cards[a]
        if tmp + cards[b] < M:
            tmp += cards[b]
            for c in range(b-1, -1, -1):
                if tmp + cards[c] <= M:
                    ans = max(ans, tmp+cards[c])
                    break
        if ans == M:
            break
    if ans == M:
        break

print(ans)
```
Leetcode 의 3 Sum 문제가 생각이 났다

어차피 3 중 for 문 돌리는 거 조금이라도 더 빨리 할 수 있지 않을까 싶어서
cards 정렬 후 각 숫자들을 최대한 큰 값부터 보면서 더해감

M 보다 작거나 같으면 ans 를 최댓값으로 update 하고
M 과 같으면 더 볼 필요가 없으므로 모두 break 해서 print

![](https://images.velog.io/images/jsh5408/post/72095fd9-bad8-4e6a-9e1e-b3b2a20edba1/image.png)

> **정석대로 할 경우**
```
for i in range (0, N):
    for j in range(i+1, N):
        for k in range (j+1, N):
            sums = cards[i]+cards[j]+cards[k]
            if sums <= M:
                ans = max(ans, sums)
```
>
![](https://images.velog.io/images/jsh5408/post/bf0e37b5-935c-41ba-a600-3f2a6989d59b/image.png)