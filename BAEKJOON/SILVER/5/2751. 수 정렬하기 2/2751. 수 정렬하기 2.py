from sys import stdin

N = int(stdin.readline())

nums = []
for i in range(N):
    n = int(stdin.readline())
    nums.append(n)

nums.sort()

for n in nums:
    print(n)