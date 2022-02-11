N = int(input())

if N == 1:
    print(0)
elif N == 2 or N == 3:
    print(1)
else:
    dp = [0]*(N+1)
    dp[2], dp[3] = 1, 1

    for n in range(4, N+1):
        tmp = n
        if n % 3 == 0:
            tmp = min(tmp, dp[n//3]+1)
        if n % 2 == 0:
            tmp = min(tmp, dp[n//2]+1)
        tmp = min(tmp, dp[n-1]+1)
        dp[n] = tmp

    print(dp[n])