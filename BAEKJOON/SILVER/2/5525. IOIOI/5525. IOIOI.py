from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
S = stdin.readline().strip()

ans = 0
P = "OI"*N

for i in range(M):
    if N*2 >= M:
        break
    if S[i] == "I":
        if S[i+1:i+1+N*2] == P:
            ans += 1

print(ans)