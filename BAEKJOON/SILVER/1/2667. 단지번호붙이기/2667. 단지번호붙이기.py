from sys import stdin

N = int(stdin.readline())

mapp = []
for _ in range(N):
    p = list(map(int, list(stdin.readline().strip())))
    mapp.append(p)

def func(i, j):
    mapp[i][j] = 0

    cnt = 0
    if i > 0 and mapp[i-1][j]:
        cnt += func(i-1, j)
    if i < N-1 and mapp[i+1][j]:
        cnt += func(i+1, j)
    if j > 0 and mapp[i][j-1]:
        cnt += func(i, j-1)
    if j < N-1 and mapp[i][j+1]:
        cnt += func(i, j+1)
    return cnt+1

ans = []
for i in range(N):
    for j in range(N):
        if mapp[i][j]:
            c = func(i, j)
            ans.append(c)

print(len(ans))
ans.sort()
for a in ans:
    print(a)