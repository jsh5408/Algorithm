from sys import stdin
import collections

T = int(stdin.readline())
nums = [0]*100
nums[0], nums[1], nums[2] = 1, 1, 1
nums[3], nums[4] = 2, 2

for i in range(5, 100):
    nums[i] = nums[i-5] + nums[i-1]

for _ in range(T):
    N = int(stdin.readline())
    print(nums[N-1])