from sys import stdin

N = int(stdin.readline())
P = list(map(int, stdin.readline().split()))

P.sort()

ans = 0

for i in range(N):
    ans += P[i] * (N-i)

print(ans)