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