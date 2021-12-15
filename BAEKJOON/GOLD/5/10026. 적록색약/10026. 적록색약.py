from sys import stdin
import sys
sys.setrecursionlimit(10**6)

N = int(stdin.readline())
painting = []

for _ in range(N):
    p = list(map(str, stdin.readline().strip()))
    painting.append(p)

a, b = 0, 0

def func(i, j, p):
    if p == "B" or p == "O":
        painting[i][j] = "X"
    else:
        painting[i][j] = "O"
    
    if i-1 >= 0 and painting[i-1][j] == p:
        func(i-1, j, p)
    if j-1 >= 0 and painting[i][j-1] == p:
        func(i, j-1, p)
    if i+1 < N and painting[i+1][j] == p:
        func(i+1, j, p)
    if j+1 < N and painting[i][j+1] == p:
        func(i, j+1, p)

for i in range(N):
    for j in range(N):
        now = painting[i][j]
        if painting[i][j] != "X" and painting[i][j] != "O":
            func(i, j, now)
            a += 1
            if now == "B":
                b += 1

for i in range(N):
    for j in range(N):
        if painting[i][j] == "O":
            func(i, j, "O")
            b += 1

print(a, b)