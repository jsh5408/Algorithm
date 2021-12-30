## 2178. 미로 탐색 - python3
https://www.acmicpc.net/problem/2178

#### 내 풀이 - 시간 초과 (재귀)
```
import sys
sys.setrecursionlimit(10**9)

N, M = map(int, sys.stdin.readline().split())

mat = []
for i in range(N):
    mat.append([0]*M)

for i in range(N):
    s = sys.stdin.readline().strip()
    for j in range(M):
        mat[i][j] = int(s[j])

ans = N*M

def func(m, i, j, cnt):
    global ans
    if i == N-1 and j == M-1:
        ans = min(ans, cnt)
        return
    if cnt > ans:
        return

    tmp = m[i][j]
    m[i][j] = 0

    if i-1 >= 0 and mat[i-1][j]:
        func(m, i-1, j, cnt+1)
    if i+1 < N and mat[i+1][j]:
        func(m, i+1, j, cnt+1)
    if j-1 >= 0 and mat[i][j-1]:
        func(m, i, j-1, cnt+1)
    if j+1 < M and mat[i][j+1]:
        func(m, i, j+1, cnt+1)
    
    m[i][j] = tmp

func(mat, 0, 0, 1)
print(ans)
```
mat 에 미로 저장

(0, 0) 부터 재귀 돌려서 현재 위치와 연결된 경로로 이동
이 때, 지나가는 곳의 값은 모두 0 으로 바꿔줌

(N-1, M-1) 에 도착하면 ans 를 최솟값으로 update

하지만... 시간초과... 예상했다...

#### 내 풀이 - 시간초과 (queue)
```
from sys import stdin
import collections

N, M = map(int, stdin.readline().split())

dp = []
mat = []
for i in range(N):
    dp.append([N*M]*M)
    mat.append([0]*M)

for i in range(N):
    s = stdin.readline().strip()
    for j in range(M):
        mat[i][j] = int(s[j])

dp[-1][-1] = 1

queue = collections.deque([(N-1, M-1)])

while queue:
    i, j = queue.popleft()

    mat[i][j] = 0

    if i == 0 and j == 0:
        break

    if i-1 >= 0 and mat[i-1][j]:
        dp[i-1][j] = dp[i][j]+1
        queue.append((i-1, j))
    if i+1 < N and mat[i+1][j]:
        dp[i+1][j] = dp[i][j]+1
        queue.append((i+1, j))
    if j-1 >= 0 and mat[i][j-1]:
        dp[i][j-1] = dp[i][j]+1
        queue.append((i, j-1))
    if j+1 < M and mat[i][j+1]:
        dp[i][j+1] = dp[i][j]+1
        queue.append((i, j+1))

print(dp[0][0])
```
끝 값부터 보면서 (0, 0) 으로 거슬러 올라가도록 함

deque 형태의 queue 를 만들어서 목적지 값인 (N-1, M-1) 저장

queue 값들을 하나씩 pop 하면서 연결된 위치를 찾아 queue 에 append
지나간 곳은 다시 볼 필요가 없으므로 mat[i][j] = 0
이 때, dp 값은 현재 경우의 수 + 1 로 update

가장 먼저 (0, 0) 에 도착한 경우가 가장 최솟값이므로 break

하지만... 이것두... 시간초과...
=> mat 의 값을 바꾸지 않고 **visited 를 따로 만들어서 사용하니까 통과 됐다**

#### 내 풀이 - 성공 (queue)
```
from sys import stdin
import collections

N, M = map(int, stdin.readline().split())

visited = []
dp = []
mat = []
for i in range(N):
    dp.append([0]*M)
    mat.append([0]*M)
    visited.append([0]*M)

for i in range(N):
    s = stdin.readline().strip()
    for j in range(M):
        mat[i][j] = int(s[j])

dp[0][0] = 1
visited[0][0] = 1

queue = collections.deque([(0, 0)])

while queue:
    i, j = queue.popleft()

    if i-1 >= 0 and visited[i-1][j] == 0 and mat[i-1][j] == 1:
        dp[i-1][j] = dp[i][j]+1
        visited[i-1][j] = 1
        queue.append((i-1, j))
    if i+1 < N and visited[i+1][j] == 0 and mat[i+1][j] == 1:
        dp[i+1][j] = dp[i][j]+1
        visited[i+1][j] = 1
        queue.append((i+1, j))
    if j-1 >= 0 and visited[i][j-1] == 0 and mat[i][j-1] == 1:
        dp[i][j-1] = dp[i][j]+1
        visited[i][j-1] = 1
        queue.append((i, j-1))
    if j+1 < M and visited[i][j+1] == 0 and mat[i][j+1] == 1:
        dp[i][j+1] = dp[i][j]+1
        visited[i][j+1] = 1
        queue.append((i, j+1))

print(dp[N-1][M-1])
```
visited 가 0 이고 mat 가 1 일 때만 queue 에 append

![](https://images.velog.io/images/jsh5408/post/f5299e93-42ea-4399-a6fe-a09a5838bcaf/image.png)

#### 다른 사람의 풀이
```
from sys import stdin
import collections

# dx[0], dy[0] => 오른쪽
# dx[1], dy[1] => 왼쪽
# dx[2], dy[2] => 아래
# dx[3], dy[3] => 위

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, stdin.readline().split())

visited = []
dp = []
mat = []
for i in range(N):
    dp.append([0]*M)
    mat.append([0]*M)
    visited.append([0]*M)

for i in range(N):
    s = stdin.readline().strip()
    for j in range(M):
        mat[i][j] = int(s[j])

dp[0][0] = 1
visited[0][0] = 1
queue = collections.deque([(0, 0)])

while queue:
    i, j = queue.popleft()

    for k in range(4):
        nx, ny = i+dx[k], j+dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and mat[nx][ny] == 1:
                dp[nx][ny] = dp[i][j] + 1
                visited[nx][ny] = 1
                queue.append((nx, ny))

print(dp[N-1][M-1])
```
4 방향에 대한 정보를 dx, dy 에 담아서 for 문으로 처리
(참고 - if 문 4 개가 for 문 보다 더 빠르다고 한다)

nx, ny 가 범위 안에 있다면 dp 값 update & visited = 1 & queue 에 append

> 참고) 2 차원 배열이 **붙어서** 주어질 경우 한줄로 처리하는 방법
```
mat = [list(map(int, list(input()))) for _ in range(N)]
```

![](https://images.velog.io/images/jsh5408/post/b6cef4ea-2ad7-45b0-ab14-d65b29c05520/image.png)