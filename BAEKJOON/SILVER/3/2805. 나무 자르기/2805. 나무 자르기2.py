from sys import stdin

N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

total = sum(trees)
trees.sort()

l = 0
r = max(trees)

while l <= r:
    m = (l+r) // 2

    tmp = 0
    for i in range(N):
        if trees[i] >= m:
            break
        tmp += trees[i]	# m 보다 작은 값들
    tmp += m*(N-i)	# 현재 높이 * m 보다 큰 값들의 개수
    
    if total - tmp < M:
        r = m-1
    else:
        l = m+1

print(l-1)