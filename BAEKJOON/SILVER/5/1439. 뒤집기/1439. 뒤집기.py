from sys import stdin

nums = list(map(int, stdin.readline().rstrip()))
zero = 0
one = 0

for i in range(1, len(nums)):
    if nums[i] - nums[i - 1] == 1:
        one += 1
    elif nums[i] - nums[i - 1] == -1:
        zero += 1

print(one) if one > zero else print(zero)