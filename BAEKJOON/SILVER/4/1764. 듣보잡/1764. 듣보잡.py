from sys import stdin

N, M = map(int, stdin.readline().split())

names = set()
ans = []

for _ in range(N):
    p = stdin.readline().strip()
    names.add(p)

for _ in range(M):
    p = stdin.readline().strip()
    if p in names:
        ans.append(p)

ans.sort()

print(len(ans))
for p in ans:
    print(p)