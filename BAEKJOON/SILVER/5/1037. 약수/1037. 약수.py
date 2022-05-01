from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

N = min(nums) * max(nums)
print(N)