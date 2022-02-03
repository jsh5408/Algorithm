from sys import stdin
import collections
import math

N = int(stdin.readline())
nums = [0] * N

for i in range(N):
    nums[i] = int(stdin.readline())

nums.sort()

# 산술평균
print(round(sum(nums)/N))

# 중앙값
print(nums[N//2])

# 최빈값
n = collections.Counter(nums)
m = 1
for k,v in n.items():
    if v > m:
        m = v
r = []
for k,v in n.items():
    if v == m:
        m = v
        r.append(k)
        if len(r) == 2:
            r.pop(0)
            break
print(r[0])

# 범위
print(nums[-1] - nums[0])