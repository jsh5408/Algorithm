from sys import stdin

N = int(stdin.readline())

nums = [0]*10001

for i in range(N):
    n = int(stdin.readline())
    nums[n] = nums[n] + 1

for i in range(10001):
    for j in range(nums[i]):
        print(i)