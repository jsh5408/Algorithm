from sys import stdin
import collections

N = int(stdin.readline())

for _ in range(N):
    n = int(stdin.readline())
    clothes = collections.defaultdict(int)
    ans = 1
    for _ in range(n):
        cloth = stdin.readline().split()
        clothes[cloth[1]] += 1
    for k, v in clothes.items():
        ans *= v+1
    print(ans-1)