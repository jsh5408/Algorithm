from sys import stdin
import collections

N = int(stdin.readline())

papers = []
for _ in range(N):
    p = list(map(int, stdin.readline().split()))
    papers.append(p)

white = 0
blue = 0

def func(si, sj, ei, ej, n):
    global white, blue

    value = papers[si][sj]
    cut = 0
    for i in range(si, ei):
        for j in range(sj, ej):
            if value != papers[i][j]:
                cut = 1
                break
        if cut:
            break
    
    if cut:
        func(si, sj, si+n//2, sj+n//2, n//2)  # 1
        func(si, sj+n//2, si+n//2, sj+n, n//2)  # 2
        func(si+n//2, sj, si+n, sj+n//2, n//2)  # 3
        func(si+n//2, sj+n//2, si+n, sj+n, n//2)  # 4
    else:
        if value == 0:
            white += 1
        else:
            blue += 1

func(0, 0, N, N, N)

print(white)
print(blue)