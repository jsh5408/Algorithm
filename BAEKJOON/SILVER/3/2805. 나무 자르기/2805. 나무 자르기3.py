from sys import stdin

N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

l = 0
r = max(trees)

while l <= r:
    m = (l+r) // 2

    tmp = 0
    for i in range(N):
        if trees[i] >= m:
            tmp += trees[i] - m
    
    if tmp < M:
        r = m-1
    else:
        l = m+1

print(r)