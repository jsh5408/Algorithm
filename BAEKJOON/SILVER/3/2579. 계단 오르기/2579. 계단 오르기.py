from sys import stdin

N = int(stdin.readline())
stairs = [0]*N
dp = [0]*N

for i in range(N):
    n = int(stdin.readline())
    stairs[i] = n

if N == 1:
    print(stairs[0])
elif N == 2:
    print(max(stairs[0]+stairs[1], stairs[1]))
else:
    dp[0] = stairs[0]
    dp[1] = max(stairs[0]+stairs[1], stairs[1])
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

    for i in range(3, N):
        dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i]+stairs[i-1])

    print(dp[-1])