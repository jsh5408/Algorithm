from sys import stdin

N = int(stdin.readline())

ans = 0
for n in range(1, N):
    s = str(n)
    M = n
    for c in s:
        M += int(c)
    if M == N:
        ans = n
        break

print(ans)