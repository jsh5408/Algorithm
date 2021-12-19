from sys import stdin
import math

A, B, V = map(int, stdin.readline().split())

if A == V:
    print(1)
else:
    V -= A
    ans = 1
    day = 0
    ans += math.ceil(V / (A-B))
    print(ans)