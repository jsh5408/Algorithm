## 1012. 유기농 배추
https://www.acmicpc.net/problem/1012

#### 내 풀이 - 성공
```
import sys
sys.setrecursionlimit(10**6)

def func(field, i, j):
    field[i][j] = 0

    if i > 0 and field[i-1][j]:
        func(field, i-1, j)
    if j > 0 and field[i][j-1]:
        func(field, i, j-1)
    if i < len(field)-1 and field[i+1][j]:
        func(field, i+1, j)
    if j < len(field[0])-1 and field[i][j+1]:
        func(field, i, j+1)

ans = []
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    field = []
    for _ in range(N):
        field.append([0]*M)

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    a = 0

    for i in range(N):
        for j in range(M):
            if field[i][j]:
                a += 1
                func(field, i, j)
    ans.append(a)

for a in ans:
    print(a)
```
`field` 값이 1 이면 재귀 돌려서 인접한 모든 배추들을 0 으로 바꿔주기

그때마다 `a + 1` 해주며 세준 지렁이를 `ans` 에 저장해서 한번에 출력

> 여기서 포인트는 
```
import sys
sys.setrecursionlimit(10**6)
```
다!!!
>
파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이므로
**setrecursionlimit** => Python이 정한 최대 재귀 깊이를 변경해줘야 함
>
참고) https://help.acmicpc.net/judge/rte/RecursionError

![](https://images.velog.io/images/jsh5408/post/5c595677-b622-4098-825a-d305fd6141eb/image.png)
