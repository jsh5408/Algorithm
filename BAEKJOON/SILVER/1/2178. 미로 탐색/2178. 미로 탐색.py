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