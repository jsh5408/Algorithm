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