from sys import stdin
import collections

N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

total = sum(trees)
trees.sort()
count = collections.Counter(trees)

if total == M:
    print(0)
else:
    idx = 0
    num = N
    if trees[idx] == 0:
        idx += count[0]
        num -= count[0]
    for t in range(1, max(trees)+1):
        if total - num < M:
            break
        total -= num 
        if t == trees[idx]:
            idx += count[t]
            num -= count[t]

    print(t-1)