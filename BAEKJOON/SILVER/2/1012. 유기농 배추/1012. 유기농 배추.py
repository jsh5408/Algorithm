import sys
sys.setrecursionlimit(10**6)

def func(field, i, j):
    field[i][j] = 0

    if i > 0 and field[i-1][j]:
        func(field, i-1, j)
    if j > 0 and field[i][j-1]:
        func(field, i, j-1)
    if i < len(field)-1 and field[i+1][j]:
        func(field, i+1, j)
    if j < len(field[0])-1 and field[i][j+1]:
        func(field, i, j+1)

ans = []
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    field = []
    for _ in range(N):
        field.append([0]*M)

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    a = 0

    for i in range(N):
        for j in range(M):
            if field[i][j]:
                a += 1
                func(field, i, j)
    ans.append(a)

for a in ans:
    print(a)