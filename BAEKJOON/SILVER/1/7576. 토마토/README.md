## 7576. 토마토 - python3
https://www.acmicpc.net/problem/7576

#### 내 풀이 - 성공
```
from sys import stdin
import collections

M, N = map(int, stdin.readline().split())
box = []
queue = collections.deque([])

for i in range(N):
    l = list(map(int, stdin.readline().strip().split()))
    for j in range(M):
        if l[j] == 1:
            queue.append([i, j])
    box.append(l)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
            queue.append([nx, ny])
            box[nx][ny] = box[x][y] + 1

ans = -1
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        ans = max(ans, box[i][j])

print(ans-1)
```
어제 7569. 토마토의 매운맛을 보고 났더니 이번 토마토는 금방 풀 수 있었다

익은 토마토의 정보 [i, j] 를 queue 에 모두 저장

x, y +- 1 연산을 하기 위해 dx, dy 리스트를 따로 만들고
queue 에서 하나씩 pop 해서 [x, y] 에 사방을 확인하는 4 가지 연산을 수행

nx, ny 가 유효한 범위고 현재 익지 않은 토마토라면 queue 에 저장
=> 다음 턴엔 익은 토마토가 되는 거니까
box 값은 box[x][y] + 1 로 누적값 저장

다시 box 를 보면서 0 이 남아있다면 -1 print
없다면 최댓값 찾아서 -1 한 값 print

![](https://images.velog.io/images/jsh5408/post/a71750f3-a414-4a3d-a61e-711c2d89b5d9/image.png)