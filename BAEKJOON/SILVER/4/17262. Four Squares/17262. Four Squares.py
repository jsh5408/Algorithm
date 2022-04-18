from sys import stdin
import math

N = int(stdin.readline())
dp = [0]*(N+1)

for i in range(1, N+1):
    tmp = int(math.sqrt(i))
    m = 4
    for j in range(tmp, 0, -1):
        m = min(m, dp[i-j*j] + 1)
    dp[i] = m

print(dp[N])