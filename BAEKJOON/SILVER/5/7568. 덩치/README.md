## 7568. 덩치 - python3
https://www.acmicpc.net/problem/7568

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())
people = []
rank = [1] * N

for i in range(N):
    x, y = map(int, stdin.readline().split())
    people.append((x, y))

for i in range(N):
    for j in range(i+1, N):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            rank[j] += 1
        elif people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1

for r in rank:
    print(r, end=" ")
```
(x, y) 의 형태로 people 에 모두 저장

이중 for 문으로 모든 사람끼리 비교해서
i 의 덩치가 더 크면 rank[i] + 1
j 의 덩치가 더 크면 rank[j] + 1
비교할 수 없으면 그냥 지나가도록 함

그러면 순위가 완성된다

![](https://images.velog.io/images/jsh5408/post/ac5c316d-1760-4636-9632-cee4a14e7c3e/image.png)