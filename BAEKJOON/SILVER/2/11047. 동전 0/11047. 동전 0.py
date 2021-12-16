from sys import stdin

N, K = map(int, stdin.readline().split())
coins = []
ans = 0

for _ in range(N):
    c = int(stdin.readline())
    coins.append(c)

for i in range(N-1, -1, -1):
    if coins[i] <= K:
        ans += K // coins[i]
        K = K % coins[i]

print(ans)