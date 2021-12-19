## 2667. 단지번호붙이기 - python3
https://www.acmicpc.net/problem/2667

#### 내 풀이 - 성공
```
from sys import stdin

N = int(stdin.readline())

mapp = []
for _ in range(N):
    p = list(map(int, list(stdin.readline().strip())))
    mapp.append(p)

def func(i, j):
    mapp[i][j] = 0

    cnt = 0
    if i > 0 and mapp[i-1][j]:
        cnt += func(i-1, j)
    if i < N-1 and mapp[i+1][j]:
        cnt += func(i+1, j)
    if j > 0 and mapp[i][j-1]:
        cnt += func(i, j-1)
    if j < N-1 and mapp[i][j+1]:
        cnt += func(i, j+1)
    return cnt+1

ans = []
for i in range(N):
    for j in range(N):
        if mapp[i][j]:
            c = func(i, j)
            ans.append(c)

print(len(ans))
ans.sort()
for a in ans:
    print(a)
```
지도를 훑어보면서 집이 있으면 그 집과 연결된 이웃집들의 개수를 세서 ans 에 append

한번 본 집들은 mapp[i][j] = 0 으로 update 하고 cnt 로 개수 count 해서 return

총 단지수인 ans 의 길이 출력하고
각 단지내 집의 수는 오름차순으로 정렬한 후 출력

> 파이썬 지역변수의 범위 참고
https://dojang.io/mod/page/view.php?id=2365

![](https://images.velog.io/images/jsh5408/post/21ff0cf1-b1a1-4f03-8167-538f29fd30e2/image.png)