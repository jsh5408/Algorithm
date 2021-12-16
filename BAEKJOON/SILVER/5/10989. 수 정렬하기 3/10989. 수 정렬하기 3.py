from sys import stdin
import collections

N = int(stdin.readline())

nums = collections.defaultdict(int)

for i in range(N):
    n = int(stdin.readline())
    nums[n] += 1

nums = sorted(nums.items())

for k, v in nums:
    for _ in range(v):
        print(k)