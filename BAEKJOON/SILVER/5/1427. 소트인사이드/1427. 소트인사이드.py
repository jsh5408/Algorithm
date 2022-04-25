from sys import stdin

N = stdin.readline().strip()
nums = [0]*len(N)

for i in range(len(N)):
    nums[i] = N[i]

nums.sort(reverse=True)
print(''.join(nums))