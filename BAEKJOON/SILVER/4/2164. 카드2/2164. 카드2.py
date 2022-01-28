from sys import stdin
from collections import deque

N = int(stdin.readline())

nums = deque([i for i in range(1, N+1)])
flag = 0
while len(nums) > 1:
    n = nums.popleft()
    if flag:
        nums.append(n)
        flag = 0
    else:
        flag = 1
print(nums[0])